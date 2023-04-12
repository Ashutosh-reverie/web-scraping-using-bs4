import pysbd
seg = pysbd.Segmenter(language="hi")
def segment_mai_text(txt_file, sent_file, segmenter):
    with open(txt_file, "r", encoding = "utf-8") as file:
        text = file.read()
    text = " ".join(text.split("\n" or "!"))
    eng_sents = seg.segment(text)
    with open(sent_file, "w+", encoding = "utf-8") as file:
        for sent in eng_sents:
            file.write(sent + "\n")

segment_mai_text("web_Scraping_mai",'web_scraping_all_paper.mai',seg)
lines=open(f"web_scraping_all_paper.mai", 'r')
mai_lines=lines.readlines()
print(len(mai_lines))  
mai_lines=set(mai_lines)
print(len(mai_lines))       