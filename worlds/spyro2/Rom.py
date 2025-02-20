"""
Module containing ROM information for Spyro 2 for Archipelago
"""
from worlds.Files import APProcedurePatch, APTokenMixin

class Spyro2ProcedurePatch(APProcedurePatch, APTokenMixin):
    """
    Definition of the APProcedurePatch to patch Spyro 2 disc images
    """
    game = "Spyro 2 Ripto's Rage!"
    hash = "9771D273C498E29AA9543C30EC00AA35"
    patch_file_ending = ".apspyro2"
    result_file_ending = ".bin"

    procedure = [
        ("apply_patches", ["options.json"]),
        ("apply_tokens", ["token_data.bin"]),
    ]
