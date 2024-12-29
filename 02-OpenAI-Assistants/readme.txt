https://learn.microsoft.com/en-us/azure/ai-services/openai/assistants-quickstart?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=command-line%2Cjavascript-keyless%2Ctypescript-keyless&pivots=ai-foundry-portal


az login --tenant 245fdc04-6bdc-4436-82a0-5d7c285b0b57


issue with logging in via browers
Sign in with Web Account Manager (WAM) on Windows
Beginning with Azure CLI version 2.61.0, Web Account Manager (WAM) is now the default authentication method on Windows. WAM is a Windows 10+ component that acts as an authentication broker. (An authentication broker is an application that runs on a user’s machine that manages the authentication handshakes and token maintenance for connected accounts.)

Using WAM has several benefits:

Enhanced security. See Conditional Access: Token protection (preview).
Support for Windows Hello, conditional access policies, and FIDO keys.
Streamlined single sign-on.
Bug fixes and enhancements shipped with Windows.
If you encounter an issue and want to revert to the previous browser-based authentication method, set the core.enable_broker_on_windows configuration property to false.

Azure CLI

Copy

Open Cloud Shell
az account clear
az config set core.enable_broker_on_windows=false
az login