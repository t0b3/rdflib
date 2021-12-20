# Recovered from https://github.com/RDFLib/rdflib/pull/1068
from rdflib import ConjunctiveGraph, Dataset, Graph, URIRef

michel = URIRef("urn:michel")
tarek = URIRef("urn:tarek")
bob = URIRef("urn:bob")
likes = URIRef("urn:likes")
hates = URIRef("urn:hates")
pizza = URIRef("urn:pizza")
cheese = URIRef("urn:cheese")

timblcardn3 = """
# N3
# Personal information in machine-readable form
#
# This (card.n3) is Tim Berners-Lee's FOAF file. It is a data file with the
#    sort of information which would be on a home page.
# This is RDF data.
# This is written in Notation3 - see http://www.w3.org/DesignIssues/Notation3
# See alternatively the RDF/XML file card.rdf generated from this.
# Use the uri <https://www.w3.org/People/Berners-Lee/card> to refer to this
#    file independent of the format.
# Use the uri <https://www.w3.org/People/Berners-Lee/card#i> to refer to Tim BL.
#
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .
@prefix doap:  <http://usefulinc.com/ns/doap#>.
@prefix :      <http://www.w3.org/2000/10/swap/pim/contact#>.
@prefix s:     <http://www.w3.org/2000/01/rdf-schema#>.
@prefix cert:  <http://www.w3.org/ns/auth/cert#>.
@prefix cc:    <http://creativecommons.org/ns#>.
@prefix dc:    <http://purl.org/dc/elements/1.1/>.
@prefix dct:   <http://purl.org/dc/terms/>.
@prefix ldp:   <http://www.w3.org/ns/ldp#>.
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#>.
@prefix geo:   <http://www.w3.org/2003/01/geo/wgs84_pos#>.
@prefix w3c:   <http://www.w3.org/data#>.
@prefix card:  <https://www.w3.org/People/Berners-Lee/card#>.
# @prefix oldcard:  <http://www.w3.org/People/Berners-Lee/card#>.
@prefix rsa:   <http://www.w3.org/ns/auth/rsa#> .
@prefix schema: <http://schema.org/>.
@prefix sioc: <http://rdfs.org/sioc/ns#>.
@prefix solid: <http://www.w3.org/ns/solid/terms#>.
@prefix space: <http://www.w3.org/ns/pim/space#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.

# About this document:
# The <> (the empty URI) means "this document".

    <>   a foaf:PersonalProfileDocument;
         cc:license <http://creativecommons.org/licenses/by-nc/3.0/>;
     dc:title "Tim Berners-Lee's FOAF file";
         foaf:maker card:i;
         foaf:primaryTopic card:i.


# Now remove any mention of it in case it gets used
#     oldcard:i = card:i .  # There is much data about oldcard:i still around


# Below we introduce a FOAF file I have write access to, which the tabulator
# will let me edit.


# Turn off this section to turn off the live editing of the FOAF file extension.
# This is where my list of people I know is:
card:i    rdfs:seeAlso <https://timbl.com/timbl/Public/friends.ttl>.       # Suggest fetch it for those reading it
card:i   solid:editableProfile <https://timbl.com/timbl/Public/friends.ttl>.
<https://timbl.com/timbl/Public/friends.ttl>
        a foaf:PersonalProfileDocument;  # Suitable place to edit
        cc:license <http://creativecommons.org/licenses/by-nc/3.0/>;
        dc:title "Tim Berners-Lee's editable profile";
        foaf:maker card:i;
        foaf:primaryTopic card:i.

########## Pointers to LDP stuff

card:i solid:oidcIssuer <https://timbl.com> . # OIDC login link
# You may trust timbl.com to log me in

card:i  solid:publicTypeIndex  <https://timbl.com/timbl/Public/PublicTypeIndex.ttl>.

card:i space:preferencesFile <https://timbl.com/timbl/Data/preferences.n3>.

card:i ldp:inbox <https://timbl.com/timbl/Public/Inbox> .

# A bot I control
card:i schema:owns <https://timblbot.inrupt.net/profile/card#me> .

# Solid Pods
card:i  space:storage  <https://timbl.solid.community/>,
  <https://timbl.inrupt.net/>,
  <https://timbl.com/timbl/Public/> .

# <https://webid.mit.edu/timbl#>
#          <http://www.w3.org/ns/pim/space#storage>
#              <https://timbl.rww.io/> .


############## Stuff about me

w3c:W3C foaf:member card:i.
<http://dig.csail.mit.edu/data#DIG> foaf:member card:i.

card:i
    s:label     "Tim Berners-Lee";   # For generic user interfaces etc

    # Using VCARD vocabulary:

    vcard:fn  "Tim Berners-Lee";

    vcard:hasAddress
        [ a    vcard:Work;
        vcard:locality "Cambridge";
        vcard:postal-code "02139";
        vcard:region "MA";
        vcard:street-address "32 Vassar Street" ];

  # Using Contact vocabulary:

    a :Male;

    :office [
        geo:location [geo:lat "42.361860"; geo:long "-71.091840"];
        :address [
            :street "32 Vassar Street";
            :street2 "MIT CSAIL Building 32";
            :city "Cambridge";
            :postalCode "02139";
            :country "USA"
    ]
    ];
    :publicHomePage <../Berners-Lee/>;
    :homePage <../Berners-Lee/>;     # hack - follows by RDFS from line above
                # The W3C structure data uses this as an IFP
#    is foaf:member of w3c:W3C;    # SYNTAX NOT IN TURTLE :-(
    :assistant card:amy;

# Using FOAF vocabulary:

    a foaf:Person;
    foaf:based_near [geo:lat "42.361860"; geo:long "-71.091840"];

    # The idea is that this is the one I would suggest you use and
    # I use for myself, which can lead to others.
    :preferredURI "https://www.w3.org/People/Berners-Lee/card#i";

    foaf:mbox <mailto:timbl@w3.org>;
    foaf:mbox_sha1sum "965c47c5a70db7407210cef6e4e6f5374a525c5c";
    foaf:openid <https://www.w3.org/People/Berners-Lee/>;
    sioc:avatar <images/timbl-image-by-Coz-cropped.jpg>;
    foaf:img <https://www.w3.org/Press/Stock/Berners-Lee/2001-europaeum-eighth.jpg>;

    foaf:family_name "Berners-Lee";
    foaf:givenname "Timothy";
    foaf:title "Sir".


card:i
    foaf:homepage <https://www.w3.org/People/Berners-Lee/>;
     foaf:mbox <mailto:timbl@w3.org>;
    #    foaf:mbox_sha1sum "1839a1cc2e719a85ea7d9007f587b2899cd94064";
     foaf:name "Timothy Berners-Lee";
     foaf:nick "TimBL", "timbl";
    #         foaf:schoolHomepage <https://www.w3.org/People/Berners-Lee>;

    foaf:account <http://twitter.com/timberners_lee>,
        <http://www.reddit.com/user/timbl/>,
        <http://en.wikipedia.org/wiki/User:Timbl>;

#        <http://identi.ca/timbl>;     #  vanished since they switch to pump.io ?

    #         foaf:workInfoHomepage <https://www.w3.org/People/Berners-Lee>;
     foaf:workplaceHomepage <https://www.w3.org/>.

card:i solid:profileHighlightColor "#00467E"; # see eg https://www.w3.org/Press/Group/Brand.html
 solid:profileBackgroundColor "#ffffff".

# Connect this profile to my MIT webid

#card:i = <https://webid.mit.edu/timbl#>.
#
#<https://webid.mit.edu/timbl#>
#          <http://www.w3.org/ns/pim/space#storage>
#              <https://timbl.rww.io/> .

########  Pointers to RWW apps I am using

#   Obsolete  --- see registration standards under solid
#
#card:i
#    <http://my-profile.eu/ns/webapp#uses> <#findMyLoc> .
#<#findMyLoc>
#    <http://my-profile.eu/ns/webapp#description>
#       "Share your location with your friends.";
#    <http://my-profile.eu/ns/webapp#endpoint>
#       <https://timbl.data.fm/test2/locator/location>;
#    <http://my-profile.eu/ns/webapp#name>
#       "FindMyLoc";
#    <http://my-profile.eu/ns/webapp#service>
#       <https://findmyloc.rww.io/>.


## Facebook
# Gone  400
# card:i owl:sameAs <http://graph.facebook.com/512908782#>.   # FB RDF feed from 2011/9

#######  Likes

# card:i  :likes <http://www.gutenberg.org/catalog/world/readfile?fk_files=2372108&pageno=11>.
#<http://www.gutenberg.org/catalog/world/readfile?fk_files=2372108&pageno=11>
#    vdc:title "Moby Dick, or, the whale".

### W3C's list of talks

#  Error 500   2016
#
# See also is too strong, this is not of interest to everyone.
# ans also is now discontinued
###    card:i s:seeAlso <https://www.w3.org/2007/11/Talks/search/query?date=All+past+and+future+talks&event=None&activity=None&name=Tim+Berners-Lee&country=None&language=None&office=None&rdfOnly=yes&submit=Submit>.

##### My Web ID cert
# As of 2012-01-14:

 <#i> cert:key  [ a cert:RSAPublicKey;
    cert:modulus

"ebe99c737bd3670239600547e5e2eb1d1497da39947b6576c3c44ffeca32cf0f2f7cbee3c47001278a90fc7fc5bcf292f741eb1fcd6bbe7f90650afb519cf13e81b2bffc6e02063ee5a55781d420b1dfaf61c15758480e66d47fb0dcb5fa7b9f7f1052e5ccbd01beee9553c3b6b51f4daf1fce991294cd09a3d1d636bc6c7656e4455d0aff06daec740ed0084aa6866fcae1359de61cc12dbe37c8fa42e977c6e727a8258bb9a3f265b27e3766fe0697f6aa0bcc81c3f026e387bd7bbc81580dc1853af2daa099186a9f59da526474ef6ec0a3d84cf400be3261b6b649dea1f78184862d34d685d2d587f09acc14cd8e578fdd2283387821296f0af39b8d8845"^^xsd:hexBinary ;

        cert:exponent "65537"^^xsd:integer ] .


#  Generate a webid cert e.g. at https://my-profile.eu/certgen.php
# (See also https://github.com/MyProfile/myprofile/blob/master/certgen.php)
#  Test a webid cert at    https://auth.my-profile.eu/auth/index.php?verbose=on







##### Things I am involved in -- DOAP

card:i is doap:developer of <http://www.w3.org/2000/10/swap/data#Cwm>,
    <http://dig.csail.mit.edu/2005/ajar/ajaw/data#Tabulator>.


# BBC Catalogue links:   # Clumsy .. need to give people URIs. Now offline :-(
# card:i foaf:homepage <http://open.bbc.co.uk/catalogue/infax/contributor/169456>;
#   s:seeAlso <http://open.bbc.co.uk/catalogue/xml/contributor/169456>.


#  Advogato is geek social networking site (2008 - 2018)
# card:i owl:sameAs <http://www.advogato.org/person/timbl/foaf.rdf#me>.

##### Identi.ca identity  (gone)
### card:i owl:sameAs <http://identi.ca/user/45563>.

#  The (2006/11) DBLP database
# Gone.
# card:i owl:sameAs <http://www4.wiwiss.fu-berlin.de/dblp/resource/person/100007>.

# Bizer et al's  RDF mashup of Amazon
# card:i owl:sameAs <http://www4.wiwiss.fu-berlin.de/bookmashup/persons/Tim+Berners-Lee>.

# <http://www4.wiwiss.fu-berlin.de/booksMeshup/books/006251587X> dc:title
#"Weaving the Web: The Original Design and Ultimate Destiny of the World Wide Web";
#    dc:creator card:i.

# More from Chris Bizer: the dbpedia scrape of Wikipedia
#   @@@ Commented out temporarily as it was getting slow from redirecting each ontology term
# <http://dbpedia.org/resource/Tim_Berners-Lee> owl:sameAs card:i.

# MIT IAP course

<http://dig.csail.mit.edu/2007/01/camp/data#course> foaf:maker card:i.

# WWW2006 stuff:
#  <#i>   owl:sameAs http://www.ecs.soton.ac.uk/~dt2/dlstuff/www2006_data#tim_berners-lee
#



####### 2011  WWW2011

<http://www.w3.org/2011/Talks/0331-hyderabad-tbl/data#talk>
    dct:title "Designing the Web for an Open Society";
    foaf:maker card:i.

<http://www.ecs.soton.ac.uk/~dt2/dlstuff/www2006_data#panel-panelk01>
    s:label  "The Next Wave of the Web (Plenary Panel)";
    :participant card:i.

<http://wiki.ontoworld.org/index.php/_IRW2006>
    :participant card:i.

<http://wiki.ontoworld.org/index.php/_IRW2006>
    dc:title "Identity, Reference and the Web workshop 2006".

card:i foaf:weblog
<http://dig.csail.mit.edu/breadcrumbs/blog/4> .
<http://dig.csail.mit.edu/breadcrumbs/blog/4>
    rdfs:seeAlso <http://dig.csail.mit.edu/breadcrumbs/blog/feed/4>; # Sigh
    dc:title "timbl's blog on DIG";
    foaf:maker card:i.

<../../DesignIssues/Overview.html>   #  Has RDFA in it
    dc:title "Design Issues for the World Wide Web";
    foaf:maker card:i.

#ends
"""


def add_stuff(graph):
    graph.add((tarek, likes, pizza))
    graph.add((tarek, likes, cheese))
    graph.add((tarek, likes, bob))
    graph.add((tarek, likes, michel))
    graph.add((michel, likes, pizza))
    graph.add((michel, likes, cheese))
    graph.add((michel, likes, tarek))
    graph.add((bob, likes, cheese))
    graph.add((bob, hates, pizza))
    graph.add((bob, hates, michel))
    graph.add((bob, likes, tarek))


def test_issue837_unique_subjects():
    graph = Graph()
    add_stuff(graph)
    assert len([sub for sub in graph.subjects()]) == 11
    assert len([sub for sub in graph.subjects(unique=True)]) == 3


def test_issue837_unique_predicates():
    graph = Graph()
    add_stuff(graph)
    assert len([pred for pred in graph.predicates()]) == 11
    assert len([pred for pred in graph.predicates(unique=True)]) == 2


def test_issue837_unique_objects():
    graph = Graph()
    add_stuff(graph)
    assert len([obj for obj in graph.objects()]) == 11
    assert len([obj for obj in graph.objects(unique=True)]) == 5


def test_issue837_unique_subject_predicates():
    graph = Graph()
    add_stuff(graph)
    assert len([sub for sub in graph.subject_predicates()]) == 11
    assert len([sub for sub in graph.subject_predicates(unique=True)]) == 4


def test_issue837_unique_predicate_objects():
    graph = Graph()
    add_stuff(graph)
    assert len([pred for pred in graph.predicate_objects()]) == 11
    assert len([pred for pred in graph.predicate_objects(unique=True)]) == 7


def test_issue837_unique_subject_objects():
    graph = Graph()
    add_stuff(graph)
    assert len([obj for obj in graph.subject_objects()]) == 11
    assert len([obj for obj in graph.subject_objects(unique=True)]) == 11


no_of_statements_in_card = 86
no_of_unique_subjects = 20
no_of_unique_predicates = 58
no_of_unique_objects = 62


def test_issue837_parse_berners_lee_card_into_graph():
    graph = Graph()
    graph.parse(data=timblcardn3, format="n3")
    assert len(list(graph.subjects())) == no_of_statements_in_card
    assert len(list(graph.subjects(unique=True))) == no_of_unique_subjects
    assert len(list(graph.predicates(unique=True))) == no_of_unique_predicates
    assert len(list(graph.objects(unique=True))) == no_of_unique_objects


def test_issue837_parse_berners_lee_card_into_conjunctivegraph_default():
    graph = ConjunctiveGraph()
    graph.parse(data=timblcardn3, format="n3")
    assert len(list(graph.subjects())) == no_of_statements_in_card
    assert len(list(graph.subjects(unique=True))) == no_of_unique_subjects
    assert len(list(graph.predicates(unique=True))) == no_of_unique_predicates
    assert len(list(graph.objects(unique=True))) == no_of_unique_objects


def test_issue837_parse_berners_lee_card_into_named_graph():
    graph = ConjunctiveGraph(identifier=URIRef("context-1"))
    graph.parse(data=timblcardn3, format="n3")
    assert len(list(graph.subjects())) == no_of_statements_in_card
    assert len(list(graph.subjects(unique=True))) == no_of_unique_subjects
    assert len(list(graph.predicates(unique=True))) == no_of_unique_predicates
    assert len(list(graph.objects(unique=True))) == no_of_unique_objects


def test_issue837_parse_berners_lee_card_into_dataset_default():

    # Workaround pending completion of identifier-as-context work
    # current W-I-P allows parsing direct to Dataset default context
    # and doesn't require the dubious creation of a graph with the
    # same context identifier as the Dataset default context.

    # graph = Dataset()

    g = Dataset()
    graph = g.graph(URIRef("urn:x-rdflib:default"))

    graph.parse(data=timblcardn3, format="n3")
    assert len(list(graph.subjects())) == no_of_statements_in_card
    assert len(list(graph.subjects(unique=True))) == no_of_unique_subjects
    assert len(list(graph.predicates(unique=True))) == no_of_unique_predicates
    assert len(list(graph.objects(unique=True))) == no_of_unique_objects


def test_issue837_parse_berners_lee_card_into_dataset_context():
    g = Dataset()
    graph = g.graph()
    graph.parse(data=timblcardn3, format="n3")
    assert len(list(graph.subjects())) == no_of_statements_in_card
    assert len(list(graph.subjects(unique=True))) == no_of_unique_subjects
    assert len(list(graph.predicates(unique=True))) == no_of_unique_predicates
    assert len(list(graph.objects(unique=True))) == no_of_unique_objects
