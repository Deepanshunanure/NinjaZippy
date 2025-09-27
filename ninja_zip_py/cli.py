import argparse
import sys
from .core import zip_files_to_7z, unzip_7z_archive

def main():
    """Main entry point for the NinjaZipPy command-line utility."""
    parser = argparse.ArgumentParser(
        description="NinjaZipPy: A Python utility for zipping and unzipping .7z archives."
    )
    # This structure mirrors a typical Unix utility interface (e.g., 'tar -c' or 'git commit')
    subparsers = parser.add_subparsers(dest='command', required=True, help='Action to perform')

    # ZIP Command
    zip_parser = subparsers.add_parser('zip', help='Zip files/folders into .7z format.')
    zip_parser.add_argument('source', type=str, help='Path to the file or folder to compress.')
    zip_parser.add_argument('output', type=str, help='Name of the output .7z archive (e.g., archive.7z).')
    
    # UNZIP Command
    unzip_parser = subparsers.add_parser('unzip', help='Unzip a .7z archive into a folder.')
    unzip_parser.add_argument('archive', type=str, help='Path to the .7z archive to extract.')
    unzip_parser.add_argument('destination', type=str, help='Path to the directory to extract files into.')

    args = parser.parse_args()

    success = False
    if args.command == 'zip':
        success = zip_files_to_7z(args.source, args.output)
    elif args.command == 'unzip':
        success = unzip_7z_archive(args.archive, args.destination)
    
    if not success:
        sys.exit(1)

if __name__ == '__main__':
    main()