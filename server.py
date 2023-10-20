from app import create_app

import argparse


def parse():
    parser = argparse.ArgumentParser(description="Arguments for BERN2 server")

    # FLASK arguments
    parser.add_argument("--host",
                        default="0.0.0.0",
                        type=str,
                        help="Host for running flask")
    parser.add_argument("--port",
                        default=5000,
                        type=int,
                        help="Port for running flask")
    parser.add_argument("--front_dev",
                        action="store_true")

    # BERN2 model arguments
    parser.add_argument("--gnormplus_home",
                        help='GNormPlus home',
                        default="./resources/GNormPlusJava",
                        type=str)
    parser.add_argument("--gnormplus_port",
                        help='GNormPlus port',
                        default=18895,
                        type=int)
    parser.add_argument("--tmvar2_home",
                        help='tmVar 2.0 home',
                        default="./resources/tmVarJava",
                        type=str)
    parser.add_argument("--tmvar2_port",
                        help='tmVar 2.0 port',
                        default=18896,
                        type=int)
    parser.add_argument("--mtner_home",
                        help='biomedical language model host',
                        default="./multi_ner",
                        type=str)
    parser.add_argument("--mtner_port",
                        help='biomedical language model port',
                        default=18894,
                        type=int)
    parser.add_argument("--gene_norm_port",
                        help='GNormPlus port',
                        default=18888,
                        type=int)
    parser.add_argument('--disease_norm_port',
                        help='Sieve port',
                        default=18892,
                        type=int)
    parser.add_argument('--cache_port',
                        help='annotation cached db port',
                        default=27017,
                        type=int)
    parser.add_argument('--gnormplus_host',
                        help='GNormPlus host',
                        default='localhost',
                        type=str)
    parser.add_argument('--tmvar2_host',
                        help='tmVar 2.0 host',
                        default='localhost',
                        type=str)
    parser.add_argument('--mtner_host',
                        help='biomedical language model host',
                        default='localhost',
                        type=str)
    parser.add_argument('--cache_host',
                        help='annotation cached db host',
                        default='localhost',
                        type=str)
    parser.add_argument('--time_format',
                        help='time format',
                        default='[%d/%b/%Y %H:%M:%S.%f]',
                        type=str)
    parser.add_argument('--max_word_len',
                        help='word max chars',
                        default=50,
                        type=int)
    parser.add_argument("--seed",
                        help='seed value',
                        default=2019,
                        type=int)
    parser.add_argument("--use_neural_normalizer", action="store_true")
    parser.add_argument("--keep_files", action="store_true")
    parser.add_argument("--no_cuda", action="store_true",
                        help="Avoid using CUDA when available")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse()
    print("Arguments:")
    for arg in vars(args):
        print("\t{}: {}".format(arg, getattr(args, arg)))

    app = create_app(args)
    app.run(host=args.host, port=int(args.port), debug=args.front_dev)
