#!/usr/bin/python
# -*- coding: utf-8 -*-

import CaboCha
from cabocha.analyzer import CaboChaAnalyzer


def _get_bunsetsu_texts(tree: CaboCha.Tree) -> list[str]:
    bunsetsus = []
    for i in range(tree.chunk_size()):
        chunk = tree.chunk(i)
        chunk_text = ""
        for j in range(chunk.token_pos, chunk.token_pos + chunk.token_size):
            token = tree.token(j)
            chunk_text += token.surface

        bunsetsus.append(chunk_text)
    return bunsetsus


def _annotate_dependency_tree(tree):
    print("\nChunks and their dependencies:")

    for i in range(tree.chunk_size()):
        chunk = tree.chunk(i)
        link = chunk.link

        # Get the text for this chunk
        chunk_text = ""
        for j in range(chunk.token_pos, chunk.token_pos + chunk.token_size):
            token = tree.token(j)
            chunk_text += token.surface

        if link >= 0:
            print(f"  Chunk {i}: '{chunk_text}' -> links to chunk {link}")
        else:
            print(f"  Chunk {i}: '{chunk_text}' (ROOT)")

    print("\nDetailed token information:")
    for i in range(tree.token_size()):
        token = tree.token(i)
        print(f"  Token {i}: {token.surface} | Features: {token.feature}")


try:
    # Create analyzer (will use system cabocharc from /opt/homebrew/etc/cabocharc)
    analyzer = CaboChaAnalyzer()
    print("✓ CaboChaAnalyzer created successfully!")

    # Test with a simple Japanese sentence
    test_sentences = [
        "太郎は花子が読んでいる本を次郎に渡した",
        "人工知能研究所",
        "子供の頃何がしたかった？",
    ]
    for test_sentence in test_sentences:
        result = analyzer.parse(test_sentence)

        print(f"\n✓ Successfully parsed: '{test_sentence}'")

        # Display parse result
        print("\nParse result (dependency tree):")

        # The result from CaboChaAnalyzer is a Tree object
        # Let's use the CaboCha API directly to get more details

        parser = CaboCha.Parser()
        tree = parser.parse(test_sentence)

        print(f"\nNumber of chunks (bunsetsu): {tree.chunk_size()}")
        # print(f"Dependency tree: {_annotate_dependency_tree(tree)}")
        print(f"Bunsetsus: {_get_bunsetsu_texts(tree)}")

except Exception as e:
    print(f"✗ Error during parsing: {e}")
