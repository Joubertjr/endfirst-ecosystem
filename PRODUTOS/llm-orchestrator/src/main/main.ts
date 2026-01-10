const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { configService: configSvc } = require('./config');

function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js'),
    },
  });

  // Em desenvolvimento, carregar do Vite dev server
  // Em produção, carregar do build
  if (process.env.NODE_ENV === 'development' || !app.isPackaged) {
    mainWindow.loadURL('http://localhost:5173');
    mainWindow.webContents.openDevTools();
  } else {
    mainWindow.loadFile(path.join(__dirname, '../renderer/index.html'));
  }
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

// IPC handlers para configuração
ipcMain.handle('config:save-provider', (_event: any, config: any) => {
  try {
    configSvc.saveProvider(config);
    return { success: true };
  } catch (error: any) {
    return { success: false, error: error?.message || 'Erro desconhecido' };
  }
});

ipcMain.handle('config:get-provider', (_event: any, id: string) => {
  return configSvc.getProvider(id);
});

ipcMain.handle('config:get-all-providers', () => {
  return configSvc.getAllProviders();
});

ipcMain.handle('config:remove-provider', (_event: any, id: string) => {
  try {
    configSvc.removeProvider(id);
    return { success: true };
  } catch (error: any) {
    return { success: false, error: error?.message || 'Erro desconhecido' };
  }
});

ipcMain.handle('config:validate-api-key', (_event: any, apiKey: string) => {
  return configSvc.validateAPIKey(apiKey);
});
