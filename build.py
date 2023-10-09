from pybtex.database.input import bibtex

# My current research interest mainly lies in Vision-Language learning, Representation Learning and Computer Vision.

def get_personal_data():
    name = ["Haoxuan You", "(有昊轩)"]
    institute = 'Columbia University'
    email = "haoxuanyou@gmail.com"
    # twitter = "Mi_Niemeyer"
    github = "Hxyou"
    linkedin = "haoxuan-you-b9872a151"
    bio_text = f"""
                <p>
                    <!-- # <span style="font-weight: bold;">Bio:</span>  -->
                    I am a fifth-year Computer Science PhD student at the Columbia University, advised by <a href="https://www.ee.columbia.edu/~sfchang/" target="_blank">Prof. Shih-Fu Chang</a> and co-advised by <a href="http://web.cs.ucla.edu/~kwchang/" target="_blank">Prof. Kai-Wei Chang</a> from UCLA. 
                    Previously I received a Bachelor dregree from <a href="https://en.xidian.edu.cn/" target="_blank">Xidian University</a> in 2018. Then I spent a gap year working as a Research Assistant in Tsinghua University advised by <a href="https://www.gaoyue.org/" target="_blank">Prof. Yue Gao</a>,
                    in the middle of which, I visited  <a href="http://mcl.usc.edu" target="_blank">MCL lab</a> in University of Southern California, advised by <a href="http://mcl.usc.edu/people/cckuo/" target="_blank">Prof. C.-C. Jay Kuo</a>.
                </p>
                <p>
                    In my Ph.D. study, I am fortunate to intern at Microsoft Azure Cognitive Services Research (Mentor: <a href="https://luoweizhou.github.io/" target="_blank">Luowei Zhou</a>), 
                    Google Research (Mentor: <a href="https://jiahuiyu.com/" target="_blank">Jiahui Yu</a>, <a href="https://scholar.google.com/citations?user=qOiCKewAAAAJ&hl=en" target="_blank">Mandy Guo</a> and <a href="http://www.jasonbaldridge.com/" target="_blank">Jason Baldridge</a>),
                    and Apple AI/ML (Mentor: <a href="http://llcao.net/" target="_blank">Liangliang Cao</a>, <a href="https://zhegan27.github.io/" target="_blank">Zhe Gan</a> and <a href="https://sites.google.com/site/yinfeiyang" target="_blank">Yinfei Yang</a>).
                </p>

                <p>
                    I work on interesting and fundamental research problems in the field of vision-and-language, with an emphasis on scalable, unified and generalizable models/methods.  Recently, I focus on three topics:
                    <ul>
                        <li><b>Vision-Language Understanding:</b> Multimodal LLM, Visual Commonsense.</li>
                        <li><b>Text-to-Image Generation:</b> Auto-regressive Text-to-Image Generation, Diffusion Model.</li>
                        <li><b>Language for Vision:</b> Language-supervised Contrastive/Generative Pre-training.</li>
                    </ul>
                </p>

                 <p>
                    <i><span style="color: red;"><b>News: I will be joining Apple AI/ML as a Research Scientist working on Foundation Models after graduation. </b></span></i>
                </p>
            
                <p>
                    <a href="https://Hxyou.github.io/assets/pdf/Phd_CV.pdf" target="_blank" style="margin-right: 15px"><i class="fa fa-address-card fa-lg"></i> CV</a>
                    <a href="mailto:haoxuanyou@gmail.com" style="margin-right: 15px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://scholar.google.com/citations?user=BhysChMAAAAJ&hl=en" target="_blank" style="margin-right: 15px"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="https://github.com/Hxyou" target="_blank" style="margin-right: 15px"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://www.linkedin.com/in/haoxuan-you-b9872a151" target="_blank" style="margin-right: 15px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                    <a href="https://twitter.com/XyouH" target="_blank" style="margin-right: 15px"><i class="fab fa-twitter fa-lg"></i> Twitter</a>
                </p>
    """
    footer = """
            <div class="col-sm-12" style="font-size:14px">
                <p>
                    Website template borrowed from <a href="https://m-niemeyer.github.io/" target="_blank">Michael Niemeyer</a>.
                </p>
            </div>
    """
    return name, institute, bio_text, footer

def get_author_dict():
    return {
        'Andreas Geiger': 'https://www.cvlibs.net/',
        }

def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='Haoxuan You', make_bold_name_2='Haoxuan You*', add_links=True):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in p.get_part('first') + p.get_part('last'): 
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if string_part_i in links.keys():
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if make_bold and string_part_i == make_bold_name_2:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name_2}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s

def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    if 'award' in entry.fields.keys():
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'html': 'Project Page', 'pdf': 'Paper', 'supp': 'Supplemental', 'video': 'Video', 'poster': 'Poster', 'code': 'Code'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    for entr in ['title', 'booktitle', 'year']:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    # s += " /" + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> </div>"""
    return s

def get_talk_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> </div>"""
    return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('talk_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_talk_entry(k, bib_data.entries[k])
    return s

def get_index_html():
    pub = get_publications_html()
    talks = None
    name, institute, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <title>{name[0] + ' @ ' + institute}</title>
  <link rel="icon" type="image/x-icon" href="assets/columbia.png">
</head>

<body>
    <div class="container">
        <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="margin-bottom: 1em;">
            <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]} </span> <span STYLE="font-size:43px; font-family:'Microsoft YaHei'">{name[1]} </span> </h3>
            </div>
            <br>
            <div class="col-md-8" style="">
                {bio_text}
            </div>
            <div class="col-md-4" style="">
                <figure>
                    <img src="assets/img/profile.jpeg" class="img-thumbnail" width="280px" alt="Profile picture">
                    <figcaption class="text-left">📷 credit to: my fiancée Xiaohui </figcaption>
                </figure>
            </div>
        </div>
        <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="">
                <h4>Selected Publications (<a href="https://scholar.google.com/citations?user=BhysChMAAAAJ&hl=en" target="_blank">Full List</a>)</h4>
                <p>  </p>
                {pub}
            </div>
        </div>
        <!-- <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="">
                <h4>Talks</h4>
                {talks}
            </div>
        </div>-->
        <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
            {footer}
        </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w') as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')