SUBDIRS := $(dir $(wildcard */Makefile))

TOPTARGETS := build clean

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
	@$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)