# Bookmarks Export Tool

> 🇫🇷 Version française plus bas

Small Windows tool written in **Python** and distributed as a standalone **.exe** that detects installed browsers and exports their **bookmarks** to HTML files using the Netscape bookmark format (compatible import in all major browsers).

---

## 🇬🇧 English
(Made with Perplexity)
### What it does

- Detects installed browsers (Chromium-based + Firefox).
- Exports bookmarks for each selected browser to:
  - `C:\export_favoris\{Browser}_{Profile}_bookmarks.html`
- Uses **Netscape Bookmark HTML** format, which can be imported into:
  - Chrome, Edge, Firefox, Brave, Opera, etc. via “Import from HTML file”.

### Download

Head to the **Releases** section and download the latest:

- `BookmarksExportTool.exe` (or the current release name)

No Python or extra setup is required on the target machine.

### Supported Windows versions

- The tool is **developed and tested on Windows 10 / 11**.
- Some libraries used (GUI, filesystem, paths) may **not be fully compatible on Windows versions older than Windows 10**.  
  Running the `.exe` on Windows 7 / 8.x is not guaranteed and is not officially supported.

### Usage (with the .exe)

1. Download `BookmarksExportTool.exe` from the Releases page.
2. Run it on the Windows machine you want to migrate.
3. A small window opens:
   - The tool detects which browsers are installed.
   - Tick the browsers you want to export bookmarks from.
   - Click **Export**.
4. HTML files are created under `C:\export_favoris`.

Examples:

- `Edge_Default_bookmarks.html`
- `Firefox_xxxxx.default-release_bookmarks.html`

These files use the **Netscape Bookmark format** (same as native browser exports).

### Importing bookmarks into another browser

#### Chrome / Edge

1. Open the browser.
2. Menu → Bookmarks / Favorites → Bookmark manager.
3. Manager menu → **Import Bookmarks**.
4. Select the generated `*_bookmarks.html` file.

#### Firefox

1. Open Firefox.
2. Menu → **Bookmarks** → **Manage bookmarks** (Library).
3. Library bar → **Import and Backup** → **Import Bookmarks from HTML…**.
4. Select the generated `*_bookmarks.html` file.

All modern browsers can import this kind of HTML bookmark file.

### For developers (build from source)

If you want to rebuild the `.exe` yourself:

Requirements (dev only):

- Windows 10 / 11 recommended  
- Python 3.10+
- PyInstaller

Install PyInstaller:
```bash
pip install pyinstaller
```

Build:
```bash
pyinstaller --onefile --noconsole export_favoris.py
```

The executable will be created in dist/BookmarksExportTool.exe (or whatever name you configure).


---

Bookmarks Export Tool est un petit outil Windows en Python, distribué sous forme d’exécutable .exe autonome, qui détecte les navigateurs installés et exporte leurs favoris dans des fichiers HTML au format Netscape (format d’export classique, importable dans tous les navigateurs).

---

## 🇫🇷 Français
(Made with Perplexity)

### Ce que fait l’outil

- Détection automatique des navigateurs présents (basés sur Chromium + Firefox).
- Export des favoris de chaque navigateur sélectionné vers :
  - `C:\export_favoris\{Navigateur}_{Profil}_favoris.html`
- Format HTML Netscape Bookmark, importable dans :
  - Chrome, Edge, Firefox, Brave, Opera, etc. via “Importer depuis un fichier HTML”.

### Téléchargement

Va dans la section Releases du dépôt et télécharge la dernière version :

- `BookmarksExportTool.exe` (ou le nom actuel du binaire)

Aucune installation de Python n’est nécessaire sur le poste cible.

### Versions de Windows supportées

- L’outil est développé et testé sur Windows 10 / 11.
- Certaines librairies utilisées (GUI, gestion des chemins, etc.) peuvent ne pas être pleinement compatibles sur des versions de Windows plus anciennes que Windows 10.
Le fonctionnement sur Windows 7 / 8.x n’est pas garanti et n’est pas officiellement supporté.

### Utilisation (avec le .exe)

1. Télécharge BookmarksExportTool.exe depuis la page des Releases.
2. Lance-le sur le poste Windows à migrer.
3. Une petite fenêtre s’ouvre :
   - L’outil détecte les navigateurs installés.
   - Coche les navigateurs dont tu veux exporter les favoris.
   - Clique sur Exporter.
4. Les fichiers HTML sont créés dans C:\export_favoris.

Exemples :

- `Edge_Default_favoris.html`
- `Firefox_xxxxx.default-release_favoris.html`

Ces fichiers utilisent le format Netscape Bookmark (le même que les exports natifs des navigateurs).

### Importer les favoris dans un autre navigateur

### Chrome / Edge

1. Ouvre le navigateur.
2. Menu → Favoris / Signets → Gestionnaire de favoris.
3. Menu du gestionnaire → Importer les favoris.
4. Sélectionne le fichier `*_favoris.html` généré.

### Firefox

1. Ouvre Firefox.
2. Menu → Marque-pages → Gérer les marque-pages (Bibliothèque).
3. Barre de la Bibliothèque → Importer et sauvegarder → Importer des marque-pages au format HTML….
4. Choisis le fichier `*_favoris.html` généré.

Tous les navigateurs modernes savent importer ce type de fichier HTML de favoris.

### Pour les développeurs (reconstruire l’exe)

Si tu veux reconstruire l’exécutable à partir des sources :

Prérequis (uniquement côté dev) :

- Windows 10 / 11 recommandé
- Python 3.10+
- PyInstaller

Installer PyInstaller :
```bash
pip install pyinstaller
```

Construire l’exécutable :
```bash
pyinstaller --onefile --noconsole export_favoris.py
```

L’exécutable sera généré dans dist/BookmarksExportTool.exe (ou le nom que tu auras choisi).
