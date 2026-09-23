# Phoenix Ecosystem Status

Live architecture and progress dashboard for the Phoenix Ecosystem.

## What is live

- Visual ecosystem map inspired by the Phoenix architecture diagram.
- Manual roadmap progress for each ecosystem part.
- Live latest-commit data from the public GitHub API.
- Automatic refresh every 5 minutes.
- Manual refresh button.
- Direct links to the latest commit of each connected repository.
- No database and no external JavaScript dependencies.

## Current route

The dashboard is stored at:

`status/index.html`

It is intentionally self-contained so it can be served by GitHub Pages, the existing Phoenix web host, or another static host without a build system.

## Important distinction

The percentage is a **manual roadmap estimate**, not an automatically calculated code-completion percentage. GitHub data is used only for live repository activity and latest commits.

## Connected repositories

- Gabirell/PhoenixBuilder
- Gabirell/PhoenixEngine
- Gabirell/HowNotToDie
- Gabirell/PhoenixBuilderDocs

Phoenix Forge and infrastructure are represented in the architecture, but are not assigned a live repository source in this first version.

## Updating the roadmap

Edit the `CONFIG.projects` array in `status/index.html` when a milestone is genuinely completed. Code activity itself updates automatically in the browser.
