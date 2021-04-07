import sys
import os
from pcbnew import *

def generate_drill_files(board, output_path):
    excellon_writer = EXCELLON_WRITER(board)

    mirror_Y_axis = False
    minimal_header = False
    merge_into_one_file = False
    use_route_command = True
    use_metric_measurement = True
    generate_drill_file = True
    generate_map_file = False
    
    excellon_writer.SetOptions(mirror_Y_axis, minimal_header, wxPoint(0, 0), merge_into_one_file)
    excellon_writer.SetRouteModeForOvalHoles(use_route_command)
    excellon_writer.SetFormat(use_metric_measurement)

    excellon_writer.CreateDrillandMapFilesSet(output_path, generate_drill_file, generate_map_file)

def generate_gerber_files(board, output_path):
    plot_controller = PLOT_CONTROLLER(board)
    plot_options = plot_controller.GetPlotOptions()
    plot_options.SetOutputDirectory(output_path)
    
    layer_info = [
        (F_Cu, "F_Cu", "Front Copper"),
        (F_Mask, "F_Mask", "Front Mask"),
        (F_Paste, "F_Paste", "Front Paste"),
        (F_SilkS, "F_SilkS", "Front Silk Screen"),
        (B_Cu, "B_Cu", "Back Copper"),
        (B_Mask, "B_Mask", "Back Mask"),
        (B_Paste, "B_Paste", "Back Paste"),
        (B_SilkS, "B_SilkS", "Back Silk Screen"),
        (Edge_Cuts, "Edge_Cuts", "Edge Cut")
    ]
    
    inner_layer_count = board.GetCopperLayerCount()
    for inner_layer in range(1, inner_layer_count-1):
        layer_info.append([inner_layer, "In{}_Cu".format(inner_layer), "Inner Copper"])
        
    for layer in layer_info:
        plot_controller.SetLayer(layer[0])
        plot_controller.OpenPlotfile(layer[1], PLOT_FORMAT_GERBER, layer[2])
        plot_controller.PlotLayer()
        plot_controller.ClosePlot()

def main():
    project_file = sys.argv[1]
    output_path = sys.argv[2]

    project_name = os.path.splitext(os.path.split(project_file)[1])[0]
    project_path = os.path.splitext(os.path.split(project_file)[0])  
    
    board = LoadBoard(project_file)

    generate_gerber_files(board, output_path)
    generate_drill_files(board, output_path)

main()
