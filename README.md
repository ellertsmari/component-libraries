# Component libraries

Teaching pages for Vefskólinn, module 4 (Connecting to the world). They show how real teams split big products into small components, and the ideas behind it: abstraction, modularity, dependencies and decoupling.

- `index.html`: the landing page
- `hanna-island.html`: Hanna (Reykjavík City) and Ísland.is (Digital Iceland) side by side
- `carbon-mui.html`: Carbon (IBM) and Material UI side by side

Open `index.html` in a browser, or serve the folder with any static server. Each page has live demos, exercises, and a bar at the top that shows the whole page in each design system.

## Editing

The files in `src/` are the sources. They are also published as Claude artifacts, which is why they have no `<!doctype>`, `<head>` or `<body>`. After changing anything in `src/`, run:

```
python3 build.py
```

This rebuilds the three pages at the root as complete HTML documents, with links between them pointing at the local files.

Facts on the pages (versions, file sizes, download numbers, the Sass 1.106.0 build failure) were checked on 20–21 October 2026.
