def parse_blockquote(markdown):
    if ">" in markdown:
        a = markdown.replace(">", "")
        res = "<blockquote>" + a.strip() + "</blockquote>"

    return res


parse_blockquote("> This is a quote")  # "<blockquote>This is a quote</blockquote>".
parse_blockquote(" > This is also a quote")  # "<blockquote>This is also a quote</blockquote>".
parse_blockquote("  >    So  Is  This")  # "<blockquote>So  Is  This</blockquote>".