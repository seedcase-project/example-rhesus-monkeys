from pathlib import Path

import seedcase_sprout.core as sp

properties = sp.PackageProperties(
    title=(
        "Impact of maternal obesity on the gestational metabolome and infant "
        "metabolome, brain, and behavioral development in rhesus macaques."
    ),
    description=(
        "Maternal gestational obesity is associated with elevated risks for "
        "neurodevelopmental disorder, including autism spectrum disorder."
    ),
)

package_path = Path(__file__).resolve().parent.parent / "datapackage.json"

updated_package_properties = sp.edit_package_properties(
    path=package_path,
    properties=properties,
)

package_path = sp.write_package_properties(
    properties=updated_package_properties, path=package_path
)
