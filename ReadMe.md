// ...existing code...
# Run

1. Start virtual environment:
   - macOS: source ./.venv/bin/activate

2. Start the MCP proxy (required):
   - npx @srbhptl39/mcp-superassistant-proxy@latest --config ./config.json --outputTransport sse

3. Start Playwright MCP server to allow controlling your open browser tabs (use the "--extension" mode to access existing open tabs like chatgpt.com):
   - npx -y @playwright/mcp@latest --extension

   Alternative (for isolated/headless runs that don't attach to existing tabs):
   - npx -y @playwright/mcp@latest --isolated --headless

4. Open chatgpt.com in your browser and allow/enable the Playwright MCP extension if prompted. The MCP server must be able to inject/communicate with the extension to control open tabs.

5. Example relevant config.json entries
   - Playwright entry (ensure the -y flag is present so npx runs non-interactively):
     ["@playwright/mcp@latest", "--extension"]
     or in config.json form:
     {
       "mcpServers": {
         "playwright": {
           "command": "npx",
           "args": ["-y", "@playwright/mcp@latest", "--extension"]
         }
       }
     }

6. Notes / Troubleshooting
   - If the MCP cannot see open tabs, confirm the Playwright extension was installed/enabled in the browser and that you started the Playwright MCP with --extension mode.
   - For headless or CI usage use --isolated --headless.
   - If you see permission prompts, accept them so the extension can interact with the page.
   - If the proxy or MCP fails, re-run the commands after activating the virtual environment and confirm your config.json path is correct.
// ...existing code...