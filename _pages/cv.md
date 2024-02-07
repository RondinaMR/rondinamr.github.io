---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

(for a detailed CV, please contact me)

Education
======
* (ongoing) Ph.D. in Control and Computer Engineering, Politecnico di Torino, 2026 (expected)
* M.S. in Computer Engineering, Politecnico di Torino, 2022
* B.S. in Computer Engineering, Politecnico di Torino, 2020

Work Experience
======
* (ongoing) University teaching assistant
  <ul class="archive__item-excerpt">
    <li>March 2023 - Present</li>
    <li>Politecnico di Torino</li>
  </ul>
* IT Technician
  <ul class="archive__item-excerpt">
    <li>October 2021 - April 2022</li>
    <li>Politecnico di Torino (Linux@Studenti)</li>
  </ul>
* Web developer
  <ul class="archive__item-excerpt">
    <li>November 2018</li>
    <li>Studio Legale VMDLaw</li>
  </ul>
* Web developer
  <ul class="archive__item-excerpt">
    <li>October 2017</li>
    <li>Studio Legale VMDLaw</li>
  </ul>
* Database Analyst
  <ul class="archive__item-excerpt">
    <li>February 2012</li>
    <li>YourCad s.r.l.</li>
  </ul>

Social, Political and Institutional Experience
======
* Member of the National Council of University Students (CNSU, Consiglio Nazionale Studenti Universitari)
  <ul class="archive__item-excerpt">
    <li>October 2019 - September 2022</li>
    <li>Ministero dell'Istruzione, dell'Università e della Ricerca (MIUR, Ministery of Education, University and Research)</li>
    <li>Rome, Italy</li>
  </ul>
* President
  <ul class="archive__item-excerpt">
    <li>2018 - 2021</li>
    <li>Alter.POLIS - A.P.S. - E.T.S. association</li>
    <li>Turin, Italy</li>
  </ul>
* Member of the Board of Governors
  <ul class="archive__item-excerpt">
    <li>September 2015 - May 2019</li>
    <li>Politecnico di Torino</li>
    <li>Turin, Italy</li>
  </ul>

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed%}
    {% include archive-single-teaching-cv.html %}
  {% endfor %}</ul>
  
[//]: # (Service and leadership)

[//]: # (======)

[//]: # (* Currently signed in to 43 different slack teams)
