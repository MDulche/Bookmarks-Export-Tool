import os
import json
import sqlite3
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

EXPORT_DIR = Path(r"C:\export_favoris")


# ---------- Détection navigateurs ----------

def detect_edge():
    base = Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "Edge"
    return base if base.exists() else None

def detect_chrome():
    base = Path(os.environ.get("LOCALAPPDATA", "")) / "Google" / "Chrome"
    return base if base.exists() else None

def detect_brave():
    base = Path(os.environ.get("LOCALAPPDATA", "")) / "BraveSoftware" / "Brave-Browser"
    return base if base.exists() else None

def detect_opera():
    # Opera stable classique
    base = Path(os.environ.get("APPDATA", "")) / "Opera Software"
    return base if base.exists() else None

def detect_firefox():
    base = Path(os.environ.get("APPDATA", "")) / "Mozilla" / "Firefox" / "Profiles"
    return base if base.exists() else None


# ---------- Génération HTML (format Netscape simplifié) ----------

def generate_html(entries, title="Bookmarks"):
    html = [
        '<!DOCTYPE NETSCAPE-Bookmark-file-1>',
        '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">',
        f'<TITLE>{title}</TITLE>',
        f'<H1>{title}</H1>',
        '<DL><p>'
    ]
    for e in entries:
        url = e.get("url")
        name = e.get("name") or url
        if url:
            # pas d’échappement avancé, suffisant pour usage interne
            html.append(f'<DT><A HREF="{url}">{name}</A>')
    html.append('</DL><p>')
    return "\n".join(html)


# ---------- Exports Chromium (Edge / Chrome / Brave / Opera) ----------

def export_chromium_bookmarks(base_path: Path, browser_name: str) -> bool:
    """
    Parcourt tous les fichiers 'Bookmarks' sous base_path et exporte un HTML par profil.
    """
    if not base_path or not base_path.exists():
        return False

    bookmark_files = list(base_path.rglob("Bookmarks"))
    if not bookmark_files:
        return False

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    ok = False

    for f in bookmark_files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue

        roots = data.get("roots", {})
        bar = roots.get("bookmark_bar") or roots.get("Bookmarks Bar") or {}
        children = bar.get("children", [])
        if not children:
            continue

        entries = []
        for item in children:
            if item.get("type") == "url" and item.get("url"):
                entries.append({"name": item.get("name"), "url": item.get("url")})

        if not entries:
            continue

        profile_name = f.parent.name
        out = EXPORT_DIR / f"{browser_name}_{profile_name}_favoris.html"
        html = generate_html(entries, title=f"{browser_name} {profile_name}")
        out.write_text(html, encoding="utf-8")
        ok = True

    return ok


def export_edge_bookmarks() -> bool:
    base = detect_edge()
    return export_chromium_bookmarks(base, "Edge")


def export_chrome_bookmarks() -> bool:
    base = detect_chrome()
    # Chrome stocke les profils sous "User Data"
    if base:
        base = base / "User Data"
    return export_chromium_bookmarks(base, "Chrome")


def export_brave_bookmarks() -> bool:
    base = detect_brave()
    # Brave : mêmes principes que Chrome (User Data)
    if base:
        base = base / "User Data"
    return export_chromium_bookmarks(base, "Brave")


def export_opera_bookmarks() -> bool:
    base = detect_opera()
    if not base:
        return False

    # Opera Stable, Opera GX, etc. — on cherche tous les Bookmarks
    return export_chromium_bookmarks(base, "Opera")


# ---------- Export Firefox (SQLite -> HTML) ----------

def export_firefox_bookmarks() -> bool:
    ff_base = detect_firefox()
    if not ff_base:
        return False

    profiles = [p for p in ff_base.iterdir() if p.is_dir()]
    if not profiles:
        return False

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    ok = False

    for profile in profiles:
        places = profile / "places.sqlite"
        if not places.exists():
            continue

        try:
            # copie temporaire pour éviter les locks si Firefox ouvert
            tmp_copy = places.parent / "places_export_tmp.sqlite"
            tmp_copy.write_bytes(places.read_bytes())

            conn = sqlite3.connect(str(tmp_copy))
            cur = conn.cursor()
            # type = 1 => bookmark, url non nulle
            cur.execute("""
                SELECT moz_bookmarks.title, moz_places.url
                FROM moz_bookmarks
                JOIN moz_places ON moz_bookmarks.fk = moz_places.id
                WHERE moz_bookmarks.type = 1 AND moz_places.url IS NOT NULL
            """)
            rows = cur.fetchall()
            conn.close()
            try:
                tmp_copy.unlink()
            except Exception:
                pass

            entries = []
            for title, url in rows:
                if not url:
                    continue
                name = title or url
                entries.append({"name": name, "url": url})

            if not entries:
                continue

            out = EXPORT_DIR / f"Firefox_{profile.name}_favoris.html"
            html = generate_html(entries, title=f"Firefox {profile.name}")
            out.write_text(html, encoding="utf-8")
            ok = True

        except Exception:
            continue

    return ok


# ---------- GUI Tkinter ----------

def main_gui():
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    root = tk.Tk()
    root.title("Export favoris navigateurs")
    root.geometry("280x230")
    root.resizable(False, False)

    tk.Label(root, text="Sélectionne les navigateurs à exporter :").pack(pady=5)

    # Détection
    edge_present   = detect_edge()   is not None
    chrome_present = detect_chrome() is not None
    brave_present  = detect_brave()  is not None
    opera_present  = detect_opera()  is not None
    ff_present     = detect_firefox() is not None

    # Cases à cocher
    vars_map = {}

    def add_check(text, present):
        var = tk.BooleanVar(value=present)
        state = "normal" if present else "disabled"
        cb = tk.Checkbutton(root, text=text, variable=var, state=state)
        cb.pack(anchor="w", padx=20)
        return var

    vars_map["Edge"]    = add_check("Edge",    edge_present)
    vars_map["Chrome"]  = add_check("Chrome",  chrome_present)
    vars_map["Brave"]   = add_check("Brave",   brave_present)
    vars_map["Opera"]   = add_check("Opera",   opera_present)
    vars_map["Firefox"] = add_check("Firefox", ff_present)

    def do_export():
        selected = [name for name, var in vars_map.items() if var.get()]
        if not selected:
            messagebox.showinfo("Info", "Sélectionne au moins un navigateur.")
            return

        done = []

        if vars_map["Edge"].get():
            if export_edge_bookmarks():
                done.append("Edge")

        if vars_map["Chrome"].get():
            if export_chrome_bookmarks():
                done.append("Chrome")

        if vars_map["Brave"].get():
            if export_brave_bookmarks():
                done.append("Brave")

        if vars_map["Opera"].get():
            if export_opera_bookmarks():
                done.append("Opera")

        if vars_map["Firefox"].get():
            if export_firefox_bookmarks():
                done.append("Firefox")

        if done:
            messagebox.showinfo(
                "Terminé",
                f"Export terminé pour : {', '.join(done)}\nDossier : {EXPORT_DIR}"
            )
            try:
                os.startfile(str(EXPORT_DIR))
            except Exception:
                pass
        else:
            messagebox.showwarning("Aucun export", "Aucun favoris n'a pu être exporté.")

    tk.Button(root, text="Exporter", command=do_export).pack(pady=15)

    root.mainloop()


if __name__ == "__main__":
    main_gui()
