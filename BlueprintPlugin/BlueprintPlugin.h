#pragma once
#pragma comment( lib, "bakkesmod.lib" )
#include "bakkesmod\plugin\bakkesmodplugin.h"

class BlueprintPlugin : public BakkesMod::Plugin::BakkesModPlugin
{
public:
	virtual void onLoad();
	virtual void onUnload();
	BlueprintPlugin();
};

