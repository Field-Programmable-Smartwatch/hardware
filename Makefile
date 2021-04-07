DEBUG_BOARD_PCB_FILE = debug-board/kicad/field_programmable_smartwatch.kicad_pcb
DEBUG_BOARD_OUTPUT = $(PWD)/debug-board/kicad

.PHONY: debug-board
debug-board:
	python plot.py $(DEBUG_BOARD_PCB_FILE) $(DEBUG_BOARD_OUTPUT)
	zip debug-board-gerber.zip $(DEBUG_BOARD_OUTPUT)/*.gbr $(DEBUG_BOARD_OUTPUT)/*.drl

.PHONY: clean
clean:
	rm -f $(DEBUG_BOARD_OUTPUT)/*.gbr $(DEBUG_BOARD_OUTPUT)/*.drl *.zip
