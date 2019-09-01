# MecaDRIL
 
ENGLISH BELOW

Ce projet regroupe le développement de notebooks jupyter en python pour
le support de l'enseignement de la mécanique générale en 1ère année de
cycle universitaire.

Développé pour l'enseignement à l'EPFL, l'ensemble est commenté et
expliqué en francais

si ce projet vous intéresse, contactez cecile.hebert@epfl.ch

********************************

This project gathers a set of python-based jupyter notebooks for the
support of the teaching of mechanics in 1st year university level

developped for teaching support at EPFL, this is explained and commented
in french, which is the language of teaching


## Release v.1.0: Content 

Current available notebooks: 

01- Coordonnées cylindriques - 3D model of cylindrical coordinates

01- Coordonnées sphériques  - 3D model of spherical coordinates

01- Coordonnees polaires - Lien entre coordonnées polaires et coordonnées cartésiennes

01-Cycloid -  Curve described by a point on a circle with rolling without slipping on a line 

01-Logan - L'agent Logan : exercice de cinématique

01-Ptolemee - Le système de Ptolémée

03-Balistique - Balistique avec et sans frottements

05-Bille sur glissiere (with video of the experiment) - Une bille est lâchée dans une glissière qui forme un looping. Si elle n'est pas lâchée d'une hauteur suffisante, elle ne complète pas le looping. De quelle hauteur faut-il la lâcher pour qu'elle complète le looping ?


## Local installation steps 

1. Dowload and install anaconda from: https://www.anaconda.com/
2. Clone repository
3. Run following in the command line: 

```
conda create --no-default-packages -n mecadril python=3.7
conda activate mecadril

conda install -c conda-forge ffmpeg
conda install -c conda-forge jupyter_latex_envs 

pip install -r requirements.txt

```

To run notebooks: 

```
ipython notebook
```

