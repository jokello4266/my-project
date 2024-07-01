"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = void 0;
const vscode = require("vscode");
function activate(context) {
    context.subscriptions.push(vscode.commands.registerCommand('run-selected-powershell-script.runpowershellscript', (uri, files) => {
        let fileName = '';
        let fileDirectory = '';
        if (typeof files !== 'undefined' && files.length > 0) {
            let url = vscode.workspace.asRelativePath(files[0].path);
            fileName = url.replace(/\\/g, '/').split('/').pop() ?? 'leeg';
            fileDirectory = url.replace(/\\/g, '/').replace(/\/[^\/]+$/, '');
        }
        let terminal = vscode.window.createTerminal();
        terminal.show();
        terminal.sendText(`cd ./${fileDirectory}`);
        terminal.sendText(`./${fileName}`);
    }));
}
exports.activate = activate;
//# sourceMappingURL=extension.js.map