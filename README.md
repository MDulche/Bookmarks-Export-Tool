# Export_Favoris

> 🇫🇷 Version française plus bas

Small Windows tool written in **Python** and distributed as a standalone **.exe** that detects installed browsers and exports their **bookmarks** to HTML files using the Netscape bookmark format (compatible import in all major browsers).[web:154][web:242][web:243][web:247]

---

## 🇬🇧 English

### What it does

- Detects installed browsers (Chromium-based + Firefox).
- Exports bookmarks for each selected browser to:
  - `C:\export_favoris\{Browser}_{Profile}_bookmarks.html`
- Uses **Netscape Bookmark HTML** format, which can be imported into:
  - Chrome, Edge, Firefox, Brave, Opera, etc. via “Import from HTML file”.[web:154][web:58][web:114][web:79]

### Download

Head to the **Releases** section and download the latest:

- `export_favoris.exe`

No Python or extra setup is required on the target machine.

### Supported Windows versions

- The tool is **developed and tested on Windows 10 / 11**.
- Some libraries used (GUI, filesystem, paths) may **not be fully compatible on Windows versions older than Windows 10**.  
  Running the `.exe` on Windows 7 / 8.x is not guaranteed and is not officially supported.[web:163][web:168][web:170]

### Usage (with the .exe)

1. Download `export_favoris.exe` from the Releases page.
2. Run it on the Windows machine you want to migrate.
3. A small window opens:
   - The tool detects which browsers are installed.
   - Tick the browsers you want to export bookmarks from.
   - Click **Export**.
4. HTML files are created under `C:\export_favoris`.

Examples:

- `Edge_Default_bookmarks.html`
- `Firefox_xxxxx.default-release_bookmarks.html`

These files use the **Netscape Bookmark format** (same as native browser exports).[web:154][web:242][web:243][web:247]

### Importing bookmarks into another browser

#### Chrome / Edge

1. Open the browser.
2. Menu → Bookmarks / Favorites → Bookmark manager.
3. Manager menu → **Import Bookmarks**.
4. Select the generated `*_bookmarks.html` file.[web:58][web:79]

#### Firefox

1. Open Firefox.
2. Menu → **Bookmarks** → **Manage bookmarks** (Library).
3. Library bar → **Import and Backup** → **Import Bookmarks from HTML…**.
4. Select the generated `*_bookmarks.html` file.[web:114]

All modern browsers can import this kind of HTML bookmark file.[web:154][web:160][web:58][web:114]

### For developers (build from source)

If you want to rebuild the `.exe` yourself:

Requirements (dev only):

- Windows 10 / 11 recommended  
- Python 3.10+
- PyInstaller

Install PyInstaller:

```bash
pip install pyinstaller
