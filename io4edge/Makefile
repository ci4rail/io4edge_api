SUBTARGETS := core_api.mk functionblock.mk inventoryv1.mk inventoryv2.mk

TOPTARGETS := build clean

$(TOPTARGETS): $(SUBTARGETS)
$(SUBTARGETS):
	$(MAKE) -f $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBTARGETS)
