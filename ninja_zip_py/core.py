import py7zr
import os
import sys
from pathlib import Path

# This Python code functionally replaces the complex COM interface management, 
# property handling (BitArchiveItem), and stream management (BitArchiveReader/Writer) 
# found in the C++ files (bitarchiveitem.cpp, bitarchivereader.cpp, etc.).

def zip_files_to_7z(source_path: str, output_archive: str) -> bool:
    """Zips a file or folder into a .7z archive."""
    source_path = Path(source_path)
    output_archive = Path(output_archive)

    if not source_path.exists():
        print(f"Error: Source path does not exist: {source_path}", file=sys.stderr)
        return False
        
    print(f"Compressing '{source_path.name}' to '{output_archive.name}'...")
    
    try:
        # Determine the name inside the archive, mimicking the C++ item property logic.
        source_name_in_archive = source_path.name
        
        # py7zr.writeall handles both files and recursive directories seamlessly, 
        # abstracting the C++'s need to track filesystem vs. buffer streams.
        with py7zr.SevenZipFile(output_archive, 'w') as archive:
            archive.writeall(source_path, source_name_in_archive)

        print("Compression successful.")
        return True
    except Exception as e:
        print(f"An error occurred during zipping: {e}", file=sys.stderr)
        return False

def unzip_7z_archive(archive_path: str, destination_dir: str) -> bool:
    """Unzips a .7z archive into a destination folder."""
    archive_path = Path(archive_path)
    destination_dir = Path(destination_dir)

    if not archive_path.exists():
        print(f"Error: Archive file does not exist: {archive_path}", file=sys.stderr)
        return False
        
    print(f"Extracting '{archive_path.name}' to '{destination_dir}'...")
    
    try:
        # Replicates the implicit directory/file creation logic of the C++ extractor.
        destination_dir.mkdir(parents=True, exist_ok=True)

        with py7zr.SevenZipFile(archive_path, mode='r') as archive:
            # Replaces the complex C++ extraction callbacks and stream routing.
            archive.extractall(path=destination_dir)
            
        print("Extraction successful.")
        return True
    except Exception as e:
        print(f"An error occurred during unzipping: {e}", file=sys.stderr)
        return False