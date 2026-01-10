const { contextBridge, ipcRenderer } = require('electron');

// Expor APIs seguras para o renderer process
contextBridge.exposeInMainWorld('electronAPI', {
  platform: process.platform,
  
  // APIs de configuração
  config: {
    saveProvider: (config: any) => ipcRenderer.invoke('config:save-provider', config),
    getProvider: (id: string) => ipcRenderer.invoke('config:get-provider', id),
    getAllProviders: () => ipcRenderer.invoke('config:get-all-providers'),
    removeProvider: (id: string) => ipcRenderer.invoke('config:remove-provider', id),
    validateAPIKey: (apiKey: string) => ipcRenderer.invoke('config:validate-api-key', apiKey),
  },
});
