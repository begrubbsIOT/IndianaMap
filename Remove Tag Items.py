from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection

# Establish portal connection - replace with URL of your portal, such as "https://inmap.maps.arcgis.com/home"
gis = GIS("EnterYourPortal/AGOL URL Here", username="EnterYourUsernameHere", password="EnterYourPasswordHere")

# Search for the group containing data your content of interest. Change this group name as needed. 
groups = gis.groups.search(query='title: "IndianaMap Content"')
group = groups[0]  

# Get items in the group
group_items = group.content()

# create a list of tag words that will be removed from this content group. First line is uppercase. Second line is lowercase. Third line is unique names/indiana.
counties = ["Vanderburgh", "Spencer", "Posey", "Warrick", "Perry", "Floyd", "Harrison", "Crawford", "Dubois", "Gibson", "Pike", "Clark", "Orange", "Washington", "Scott", "Daviess", "Martin", "Knox", "Jefferson", "Switzerland", "Lawrence", "Ohio", "Jackson", "Greene", "Jennings", "Sullivan", "Dearborn", "Ripley", "Brown", "Monroe", "Bartholomew", "Decatur", "Owen", "Franklin", "Clay", "Vigo", "Morgan", "Johnson", "Shelby", "Union", "Rush", "Fayette", "Putnam", "Hendricks", "Marion", "Parke", "Hancock", "Wayne", "Henry", "Vermillion", "Boone", "Montgomery", "Hamilton", "Randolph", "Fountain", "Madison", "Delaware", "Tipton", "Clinton", "Warren", "Tippecanoe", "Howard", "Blackford", "Jay", "Grant", "Carroll", "Benton", "Cass", "White", "Wells", "Adams", "Miami", "Huntington", "Wabash", "Pulaski", "Fulton", "Newton", "Jasper", "Allen", "Whitley", "Starke", "Kosciusko", "Marshall", "Noble", "Dekalb", "Porter", "Lake", "Laporte", "St Joseph", "Elkhart", "Lagrange", "Steuben"]
# counties = ["vanderburgh", "spencer", "posey", "warrick", "perry", "floyd", "harrison", "crawford", "dubois", "gibson", "pike", "clark", "orange", "washington", "scott", "daviess", "martin", "knox", "jefferson", "switzerland", "lawrence", "ohio", "jackson", "greene", "jennings", "sullivan", "dearborn", "ripley", "brown", "monroe", "bartholomew", "decatur", "owen", "franklin", "clay", "vigo", "morgan", "johnson", "shelby", "union", "rush", "fayette", "putnam", "hendricks", "marion", "parke", "hancock", "wayne", "henry", "vermillion", "boone", "montgomery", "hamilton", "randolph", "fountain", "madison", "delaware", "tipton", "clinton", "warren", "tippecanoe", "howard", "blackford", "jay", "grant", "carroll", "benton", "cass", "white", "wells", "adams", "miami", "huntington", "wabash", "pulaski", "fulton", "newton", "jasper", "allen", "whitley", "starke", "kosciusko", "marshall", "noble", "dekalb", "porter", "lake", "laporte", "st joseph", "elkhart", "lagrange", "steuben"]
# counties = ["dekalb", "laporte", "lagrange", "indiana", "Indiana"]


# Iterate through items in the group to update tags
for item in group_items:
    if item.tags:  # Check if tags exist
        new_tags = [tag for tag in item.tags if all(county not in tag and f"{county} County" not in tag for county in counties)]
        item.update(item_properties={"tags": new_tags})
        print(f"Updated tags for item: {item.title}")
    else:
        print(f"No tags to update for item: {item.title}")





