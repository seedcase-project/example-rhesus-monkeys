from pathlib import Path

import seedcase_sprout.core as sp

package_path = Path(__file__).resolve().parent.parent

current_properties = sp.read_properties(
    path=sp.PackagePath(package_path).properties(),
)

updated_properties = sp.PackageProperties(
    title=(
        "Impact of maternal obesity on the gestational metabolome and infant "
        "metabolome, brain, and behavioral development in rhesus macaques."
    ),
    description=(
        "Maternal gestational obesity is associated with elevated risks for "
        "neurodevelopmental disorder, including autism spectrum disorder."
    ),
)

updated_package_properties = sp.update_package_properties(
    current_properties=current_properties,
    update_properties=updated_properties,
)

sp.write_package_properties(
    properties=updated_package_properties,
    path=sp.PackagePath(package_path).properties(),
)
