import google.generativeai as genai
import PIL.Image
import os

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


sample_file = PIL.Image.open('spiderman_sg_1.jpeg')
model = genai.GenerativeModel("gemini-1.5-flash-001")

page = """
<div id="page-1" class="page revamp-review-page">

<h2 class="page-title">The Lords of the Rings: The Rings of Power Season 2 (Amazon Prime) review</h2>
<p class="rtecenter"><span class="image-caption-container"><img alt="Image: Prime Video" src="https://assets.hardwarezone.com/img/2024/08/ROP_01.jpg" style="height:447px; width:800px" title="Image: Prime Video"><div class="image-caption">Image: Prime Video</div></span></p>

<p>After two seasons, <strong>The Lord of the Rings:</strong> <strong>The Rings of Power</strong>, Amazon Prime’s imagination of Middle-earth, is beginning to feel like it's treading familiar ground – even if this review is based on only the first three episodes that’s available for streaming now. The story developments so far – Halbrand turning out to be Sauron in disguise, the Southlands transforming into Mordor, and the "Stranger" hinting at a character we already know – seem less like surprising twists and more like the inevitable unfolding of a well-worn tale.</p>

<p>The series is steeped in a sense of destiny, perhaps intentionally. Based on appendices from J.R.R. Tolkien’s The Lord of the Rings, it aims to chronicle the rise of Sauron and the events that led to the alliance between elves and men in the Second Age. Yet, while it is understandable that certain story beats need to be covered – Sauron's deception, the creation of the 19 Rings of Power, the establishment of the show's numerous main and side characters – there’s a distinct feeling that the series is more concerned with checking boxes than it is with telling a fresh, dynamic story.</p>

<p>It’s evident that creators Patrick McKay and J.D. Payne have immersed themselves deeply in Tolkien’s world, and there’s some enjoyment to be found in seeing how they connect the dots between the various pieces of Middle-earth lore. The way they draw parallels between the precious metal Mithril, the legendary Silmarils, and the dwarven downfall is inventive, even if they have to skirt around elements from prequel<strong> The Silmarillion</strong>, to which Amazon lacks rights (yup, the company is only allowed to draw materials from The Lord of the Rings). However, this attention to detail often comes at the cost of narrative momentum. For example, the revelation of Halbrand’s identity as Sauron was kept under wraps far beyond the point where it was still interesting in the first season. Season two continues this trend, with Sauron disguised yet again, this time as Annatar, the Lord of Gifts – a guise so thin that it’s hard to believe even the elves could be fooled.</p>

<p><span class="image-caption-container"><img alt="Image: Prime Video" src="https://assets.hardwarezone.com/img/2024/08/ROP_02.jpg" style="height:450px; width:800px" title="Image: Prime Video"><div class="image-caption">Image: Prime Video</div></span></p>

<p>At first glance, The Rings of Power has all the components of a grand fantasy epic such as sweeping landscapes, epic battles, and an expansive cast. But when viewed up close, the show often feels constrained by its own sense of importance. There's a stiffness to many of the scenes, a reluctance to let the characters breathe and simply exist within their world. The dialogue, much like Tolkien’s original prose, tends to be lofty and serious, but without the playfulness that made Peter Jackson’s film adaptations so memorable.</p>

<p>Jackson’s films found a way to inject light-hearted moments without detracting from the epic scale — think of Pippin’s clumsiness in Moria for instance. Such small, human touches brought a sense of relatability to the larger-than-life events unfolding around them. In contrast, The Rings of Power often seems to lack these moments of levity, making its attempts at emotional depth feel somewhat forced. When the show tries to mimic iconic scenes, it often lacks the character nuance that made the original so impactful.</p>

<p>The series also has a habit of focusing on the grander narrative at the expense of the smaller, more intimate moments that could enrich its characters. While there are visually stunning scenes, such as the glowing tree of the Elves, these are often overshadowed by a score that feels overly insistent on reminding the viewer of the show’s significance. The dialogue, meanwhile, is mostly functional, lacking the metaphorical richness of Tolkien's own writing. Instead, we get lines that sound more like modern corporate updates than the lyrical storytelling one might expect from a series rooted in Middle-earth's deep mythology.</p>

<p><span class="image-caption-container"><img alt="Image: Prime Video" src="https://assets.hardwarezone.com/img/2024/08/ROP_03.jpg" style="height:450px; width:800px" title="Image: Prime Video"><div class="image-caption">Image: Prime Video</div></span></p>

<p>Despite these issues, there are signs of improvement as season two progresses. The plotlines start to converge, leading to more dynamic interactions between characters who had previously been isolated. This culminates in some well-executed action sequences, including a magical sandstorm conjured by the Stranger that, while exciting, still suffers from the show’s tendency to lean on heavy-handed dialogue and obvious reveals. The frustration here is not just with the clunky exposition but also with the missed opportunities to explore the more unique corners of Middle-earth. Instead of delving into the daily lives of Numenor’s citizens or uncovering the quirks of its culture, we’re often stuck in repetitive political machinations that feel all too familiar.</p>

<p>In the end, The Rings of Power Season 2 feels like a show that is both bound by its source material and afraid to stray too far from it. It’s trapped in a cycle of recreating what has come before, rather than finding new ways to tell its story. The show’s tragedy is much like that of the character Celebrimbor, who, in his quest to capture the light of the Silmarils, ends up creating something that feels like a pale imitation of the original.</p>

<p>There’s still hope for The Rings of Power to find its own voice as we still have five more episodes (Season 2 has eight episodes), but for now, it remains caught between its reverence for Tolkien’s work and the need to offer something new to viewers.</p>

<p><br>
<em>The Lord of the Rings: Rings of Power is available for streaming now on Amazon Prime, available for $4.99/mth. <a href="https://www.primevideo.com/offers/nonprimehomepage/ref=dv_web_force_root" target="_blank">Click here to subscribe</a>.</em></p>
											</div>
"""


response = model.generate_content([page, "Give an advice whether I should watch the tv series"], stream=True)

for text_chunks in response: 
    print(text_chunks.text)


# response2 = model.generate_content(["tell me what's going on in this picture", sample_file])
# print(response2.text)