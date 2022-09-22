import basyx.aas.model as model
import basyx.aas.adapter.json
import basyx.aas.adapter.aasx as aasx
from pathlib import Path




new_object_store: model.DictObjectStore[model.Identifiable] = model.DictObjectStore()
new_file_store = aasx.DictSupplementaryFileContainer()

with aasx.AASXReader("MyAASXPackage.aasx") as reader:
    # Read all contained AAS objects and all referenced auxiliary files
    # In contrast to the AASX Package Explorer, we are not limited to a single XML part in the package, but instead we
    # will read the contents of all included JSON and XML parts into the ObjectStore
    reader.read_into(object_store=new_object_store,
                     file_store=new_file_store)


print(new_object_store._backend.items())
if model.Identifier in new_object_store:
    print("its there")

# test = new_object_store.json()
# print(test)
# print("#############################")
