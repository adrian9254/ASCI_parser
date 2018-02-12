from modules import BOM_parser_re

parser = BOM_parser_re.GetBOM()

parser.get_bom_data("BOM_files/789268_.BOM")

print(parser.bom)