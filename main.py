import os
import click
import logging
import brotli
import danmu_pb2

from wordcloud import WordCloud, STOPWORDS


_logger = logging.Logger(__name__)
_logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
_logger.addHandler(ch)


@click.command()
@click.option('--input', '-i', 'input_path', required=True, type=str)
@click.option('--background_color', '-b', 'background_color', required=True, default="white", type=str)
@click.option('--max_words', '-m', 'max_words', required=True, default=500, type=int)
@click.option('--font_path', '-f', 'font_path', required=True, default="SourceHanMono.ttc", type=str)
@click.option('--width', '-w', 'width', required=True, default=1920, type=int)
@click.option('--height', '-h', 'height', required=True, default=1080, type=int)
@click.option('--out', '-o', 'outpath', required=True, type=str)
def main(input_path, background_color, max_words, font_path, width, height, outpath):
    danmu_data = []
    _logger.info(f"start read {input_path}")
    for path in sorted(os.listdir(f"{input_path}")):
        with open(f"{input_path}/{path}", "rb") as f:
            out = brotli.decompress(bytearray(f.read()))
            danmu = danmu_pb2.Danmu()
            danmu.ParseFromString(out)
            danmu_data.extend([
                bulletInfo.content
                for entry in danmu.entry
                for bulletInfo in entry.bulletInfo
            ])
    _logger.info(f"find danmu count {len(danmu_data)}")
    wc = WordCloud(
        background_color=background_color,
        max_words=max_words,
        stopwords=STOPWORDS,
        font_path=font_path,
        width=width, height=height
    ).generate(" ".join(danmu_data))
    wc.to_file(f"{outpath}")
    _logger.info(f"generate WordCloud to file {outpath} end")


main()
