from pathlib import Path

import seedcase_sprout.core as sp

properties = sp.PackageProperties(
    name="maternal-obesity-rhesus-monkeys",
    title=(
        "Impact of maternal obesity on the gestational metabolome and infant "
        "metabolome, brain, and behavioral development in rhesus macaques"
    ),
    description=(
        "Maternal gestational obesity is associated with elevated risks for "
        "neurodevelopmental disorder, including autism spectrum disorder. However, the "
        "mechanisms by which maternal adiposity influences fetal developmental "
        "programming remain to be elucidated. We aimed to understand the impact of "
        "maternal obesity on the metabolism of both pregnant mothers and their "
        "offspring, as well as on metabolic, brain, and behavioral development of "
        "offspring by utilizing metabolomics, protein, and behavioral assays in a "
        "non-human primate model. "
    ),
    contributors=[
        sp.ContributorProperties(
            title="Yu Hasegawa",
            path="https://bolling.foodsci.wisc.edu/staff/hasegawa-phd-yu/",
            roles=["creator"],
        ),
        sp.ContributorProperties(
            title="John Capitanio",
            path="https://psychology.ucdavis.edu/people/john-capitanio",
            roles=["creator"],
        ),
        sp.ContributorProperties(
            title="Mari Golub",
            path="https://www.etox.ucdavis.edu/people/mari-golub",
            roles=["creator"],
        ),
        sp.ContributorProperties(
            title="Judith Van de Waters",
            path="https://profiles.ucdavis.edu/judy.vandewater",
            roles=["creator"],
        ),
        sp.ContributorProperties(
            title="Catherine VandeVoort",
            path="https://profiles.ucdavis.edu/catherine.vandevoort",
            roles=["creator"],
        ),
        sp.ContributorProperties(
            title="Cheryl Walker",
            path="https://pod.ucdavis.edu/people/cheryl-walker",
            roles=["creator"],
        ),
        sp.ContributorProperties(
            title="Carolyn Slupsky",
            path="https://nutrition.ucdavis.edu/people/carolyn-slupsky",
            roles=["creator"],
        ),
    ],
    sources=[
        sp.SourceProperties(
            title=(
                "Impact of maternal obesity on the gestational metabolome and infant "
                "metabolome, brain, and behavioral development in rhesus macaques"
            ),
            path="https://zenodo.org/records/7055715",
        )
    ],
    licenses=[
        sp.LicenseProperties(
            name="CCO_1.0",
            path="https://creativecommons.org/publicdomain/zero/1.0/legalcode",
            title="CCO 1.0 UNIVERSAL",
        )
    ],
)

# Create the path to the package
package_path = Path(__file__).resolve().parent.parent
package_path = sp.create_package_properties(properties=properties, path=package_path)
