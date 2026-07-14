---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

---
<p class="archive__item-excerpt__publication">
  <b>Icon legend</b>:
  <i class="fa fa-file-pdf-o"></i> PDF &nbsp;
  <i class="ai ai-arxiv"></i> arXiv (preprint, not peer-reviewed) &nbsp;
  <i class="ai ai-doi"></i> DOI &nbsp;
  <i class="ai ai-archive"></i> Institutional repository (PoliTO IRIS) &nbsp;
  <i class="ai ai-zenodo"></i> Zenodo (supplementary material) &nbsp;
  <i class="fa-brands fa-git-alt"></i> Code repository &nbsp;
  <i class="fa fa-link"></i> Other link
</p>

