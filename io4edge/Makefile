SUBTARGETS := core_api.mk functionblock.mk inventory.mk

TOPTARGETS := build clean

$(TOPTARGETS): $(SUBTARGETS)
$(SUBTARGETS):
	$(MAKE) -f $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBTARGETS)
