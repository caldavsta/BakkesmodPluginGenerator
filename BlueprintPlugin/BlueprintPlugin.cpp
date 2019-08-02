#include "BlueprintPlugin.h"
BAKKESMOD_PLUGIN(BlueprintPlugin, "BlueprintPlugin ", "0.1", PLUGINTYPE_FREEPLAY);

BlueprintPlugin::BlueprintPlugin()
{

}

void BlueprintPlugin::onLoad()
{
	
}

void BlueprintPlugin::onUnload()
{
	cvarManager->backupCfg("./bakkesmod/cfg/config.cfg");
}