import server

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser('MyNote Options.')
    parser.add_argument('--static-file-path', help='...', default='./static')
    parser.add_argument('--template-file-path', help='...', default='./template')
    parser.add_argument('--notes-file-path', help='...')
    args = parser.parse_args()
    if not args.notes_file_path:
        parser.error('You must specify the notes file path')
    server.start(args.static_file_path, args.template_file_path, args.notes_file_path)

