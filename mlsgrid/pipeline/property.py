from mlsgrid.pipeline.interface import Pipeline

pipeline = Pipeline(
    name="Property",
    resource="Property",
    transform=lambda rows: [
        {
            "id": row.get("@odata.id"),
            "AccessibilityFeatures": [i for i in row["AccessibilityFeatures"]]
            if row.get("AccessibilityFeatures")
            else [],
            "ACT_ActiveOpenHouseCount": row.get("ACT_ActiveOpenHouseCount"),
            "AdditionalParcelsYN": row.get("AdditionalParcelsYN"),
            "Appliances": [i for i in row["Appliances"]]
            if row.get("Appliances")
            else [],
            "AssociationYN": row.get("AssociationYN"),
            "BathroomsFull": row.get("BathroomsFull"),
            "BathroomsHalf": row.get("BathroomsHalf"),
            "BathroomsTotalInteger": row.get("BathroomsTotalInteger"),
            "BedroomsTotal": row.get("BedroomsTotal"),
            "BuyerAgencyCompensation": row.get("BuyerAgencyCompensation"),
            "BuyerAgencyCompensationType": row.get("BuyerAgencyCompensationType"),
            "BuyerOfficeKey": row.get("BuyerOfficeKey"),
            "CoBuyerOfficeKey": row.get("CoBuyerOfficeKey"),
            "CommunityFeatures": [i for i in row["CommunityFeatures"]]
            if row.get("CommunityFeatures")
            else [],
            "ConstructionMaterials": [i for i in row["ConstructionMaterials"]]
            if row.get("ConstructionMaterials")
            else [],
            "Cooling": [i for i in row["Cooling"]] if row.get("Cooling") else [],
            "CountyOrParish": row.get("CountyOrParish"),
            "CoveredSpaces": row.get("CoveredSpaces"),
            "DirectionFaces": row.get("DirectionFaces"),
            "Disclosures": [i for i in row["Disclosures"]]
            if row.get("Disclosures")
            else [],
            "ACT_ElementaryOther": row.get("ACT_ElementaryOther"),
            "ElementarySchool": row.get("ElementarySchool"),
            "ACT_EstimatedTaxes": row.get("ACT_EstimatedTaxes"),
            "ACT_ETJExtraTerritorialJurdn": row.get("ACT_ETJExtraTerritorialJurdn"),
            "ExteriorFeatures": [i for i in row["ExteriorFeatures"]]
            if row.get("ExteriorFeatures")
            else [],
            "ACT_FEMAFloodPlain": row.get("ACT_FEMAFloodPlain"),
            "Fencing": [i for i in row["Fencing"]] if row.get("Fencing") else [],
            "FireplacesTotal": row.get("FireplacesTotal"),
            "Flooring": [i for i in row["Flooring"]] if row.get("Flooring") else [],
            "FoundationDetails": [i for i in row["FoundationDetails"]]
            if row.get("FoundationDetails")
            else [],
            "GarageSpaces": row.get("GarageSpaces"),
            "GreenEnergyEfficient": [i for i in row["GreenEnergyEfficient"]]
            if row.get("GreenEnergyEfficient")
            else [],
            "GreenSustainability": [i for i in row["GreenSustainability"]]
            if row.get("GreenSustainability")
            else [],
            "ACT_GuestAccommodatonDesc": row.get("ACT_GuestAccommodatonDesc"),
            "Heating": [i for i in row["Heating"]] if row.get("Heating") else [],
            "HighSchool": [i for i in row["HighSchool"]]
            if row.get("HighSchool")
            else [],
            "HorseAmenities": [i for i in row["HorseAmenities"]]
            if row.get("HorseAmenities")
            else [],
            "HorseYN": row.get("HorseYN"),
            "ACT_IDXOptInYN": row.get("ACT_IDXOptInYN"),
            "InteriorFeatures": [i for i in row["InteriorFeatures"]]
            if row.get("InteriorFeatures")
            else [],
            "InternetAddressDisplayYN": row.get("InternetAddressDisplayYN"),
            "InternetAutomatedValuationDisplayYN": row.get(
                "InternetAutomatedValuationDisplayYN"
            ),
            "InternetConsumerCommentYN": row.get("InternetConsumerCommentYN"),
            "InternetEntireListingDisplayYN": row.get("InternetEntireListingDisplayYN"),
            "ACT_LastChangeTimestamp": row.get("ACT_LastChangeTimestamp"),
            "ACT_LastChangeType": row.get("ACT_LastChangeType"),
            "ACT_LastHumanModificationTimestamp": row.get(
                "ACT_LastHumanModificationTimestamp"
            ),
            "ACT_LaundryLocation": row.get("ACT_LaundryLocation"),
            "Levels": [i for i in row["Levels"]] if row.get("Levels") else [],
            "ListAgentAOR": "Austin Board Of Realtors",
            "ListAgentDirectPhone": row.get("ListAgentDirectPhone"),
            "ListAgentEmail": row.get("ListAgentEmail"),
            "ListAgentFullName": row.get("ListAgentFullName"),
            "ListAgentKey": row.get("ListAgentKey"),
            "ListAgentMlsId": row.get("ListAgentMlsId"),
            "ListAOR": row.get("ListAOR"),
            "ListingContractDate": row.get("ListingContractDate"),
            "ListingId": row.get("ListingId"),
            "ListingKey": row.get("ListingKey"),
            "ListOfficeKey": row.get("ListOfficeKey"),
            "ListOfficeMlsId": row.get("ListOfficeMlsId"),
            "ListOfficeName": row.get("ListOfficeName"),
            "ListOfficePhone": row.get("ListOfficePhone"),
            "ListPrice": row.get("ListPrice"),
            "LivingArea": row.get("LivingArea"),
            "LivingAreaSource": row.get("LivingAreaSource"),
            "LotFeatures": [i for i in row["LotFeatures"]]
            if row.get("LotFeatures")
            else [],
            "LotSizeAcres": row.get("LotSizeAcres"),
            "LotSizeSquareFeet": row.get("LotSizeSquareFeet"),
            "MainLevelBedrooms": row.get("MainLevelBedrooms"),
            "MajorChangeTimestamp": row.get("MajorChangeTimestamp"),
            "MajorChangeType": row.get("MajorChangeType"),
            "MiddleOrJuniorSchool": row.get("MiddleOrJuniorSchool"),
            "MLSAreaMajor": row.get("MLSAreaMajor"),
            "MlsStatus": row.get("MlsStatus"),
            "NewConstructionYN": row.get("NewConstructionYN"),
            "ACT_NumDining": row.get("ACT_NumDining"),
            "ACT_NumLiving": row.get("ACT_NumLiving"),
            "ACT_OpenHouseCount": row.get("ACT_OpenHouseCount"),
            "ACT_OpenHousePublicCount": row.get("ACT_OpenHousePublicCount"),
            "OriginalEntryTimestamp": row.get("OriginalEntryTimestamp"),
            "OriginalListPrice": row.get("OriginalListPrice"),
            "OriginatingSystemName": row.get("OriginatingSystemName"),
            "OtherStructures": [i for i in row["OtherStructures"]]
            if row.get("OtherStructures")
            else [],
            "ParcelNumber": row.get("ParcelNumber"),
            "ParkingFeatures": [i for i in row["ParkingFeatures"]]
            if row.get("ParkingFeatures")
            else [],
            "ParkingTotal": row.get("ParkingTotal"),
            "PatioAndPorchFeatures": [i for i in row["PatioAndPorchFeatures"]]
            if row.get("PatioAndPorchFeatures")
            else [],
            "PoolFeatures": [i for i in row["PoolFeatures"]]
            if row.get("PoolFeatures")
            else [],
            "PoolPrivateYN": row.get("PoolPrivateYN"),
            "PreviousListPrice": row.get("PreviousListPrice"),
            "PropertyCondition": [i for i in row["PropertyCondition"]]
            if row.get("PropertyCondition")
            else [],
            "PropertySubType": row.get("PropertySubType"),
            "PropertyType": row.get("PropertyType"),
            "PublicRemarks": row.get("PublicRemarks"),
            "Roof": [i for i in row["Roof"]] if row.get("Roof") else [],
            "Sewer": [i for i in row["Sewer"]] if row.get("Sewer") else [],
            "SpaFeatures": [i for i in row["SpaFeatures"]]
            if row.get("SpaFeatures")
            else [],
            "SpecialListingConditions": [i for i in row["SpecialListingConditions"]]
            if row.get("SpecialListingConditions")
            else [],
            "StandardStatus": row.get("StandardStatus"),
            "ACT_StatusContractualSearchDate": row.get(
                "ACT_StatusContractualSearchDate"
            ),
            "SubAgencyCompensation": row.get("SubAgencyCompensation"),
            "SubAgencyCompensationType": row.get("SubAgencyCompensationType"),
            "SubdivisionName": row.get("SubdivisionName"),
            "SyndicateTo": [i for i in row["SyndicateTo"]]
            if row.get("SyndicateTo")
            else [],
            "SyndicationRemarks": row.get("SyndicationRemarks"),
            "TaxAssessedValue": row.get("TaxAssessedValue"),
            "ACT_TaxFilledSqftTotal": row.get("ACT_TaxFilledSqftTotal"),
            "TaxLegalDescription": row.get("TaxLegalDescription"),
            "TaxMapNumber": row.get("TaxMapNumber"),
            "TaxYear": row.get("TaxYear"),
            "ACT_UnitStyle": row.get("ACT_UnitStyle"),
            "Utilities": [i for i in row["Utilities"]] if row.get("Utilities") else [],
            "View": [i for i in row["View"]] if row.get("View") else [],
            "VirtualTourURLUnbranded": row.get("VirtualTourURLUnbranded"),
            "WaterfrontFeatures": [i for i in row["WaterfrontFeatures"]]
            if row.get("WaterfrontFeatures")
            else [],
            "WaterfrontYN": row.get("WaterfrontYN"),
            "WaterSource": [i for i in row["WaterSource"]]
            if row.get("WaterSource")
            else [],
            "WindowFeatures": [i for i in row["WindowFeatures"]]
            if row.get("WindowFeatures")
            else [],
            "YearBuilt": row.get("YearBuilt"),
            "YearBuiltSource": row.get("YearBuiltSource"),
            "ModificationTimestamp": row.get("ModificationTimestamp"),
            "PhotosCount": row.get("PhotosCount"),
            "PhotosChangeTimestamp": row.get("PhotosChangeTimestamp"),
            "City": row.get("City"),
            "Country": row.get("Country"),
            "Directions": row.get("Directions"),
            "Latitude": row.get("Latitude"),
            "Longitude": row.get("Longitude"),
            "PostalCode": row.get("PostalCode"),
            "StateOrProvince": row.get("StateOrProvince"),
            "StreetName": row.get("StreetName"),
            "StreetNumber": row.get("StreetNumber"),
            "StreetNumberNumeric": row.get("StreetNumberNumeric"),
            "StreetSuffix": row.get("StreetSuffix"),
            "UnparsedAddress": row.get("UnparsedAddress"),
            "MlgCanView": row.get("MlgCanView"),
        }
        for row in rows
    ],
    schema=[
        {"name": "id", "type": "STRING"},
        {"name": "AccessibilityFeatures", "type": "STRING", "mode": "REPEATED"},
        {"name": "ACT_ActiveOpenHouseCount", "type": "STRING"},
        {"name": "AdditionalParcelsYN", "type": "BOOLEAN"},
        {"name": "Appliances", "type": "STRING", "mode": "REPEATED"},
        {"name": "AssociationYN", "type": "BOOLEAN"},
        {"name": "BathroomsFull", "type": "NUMERIC"},
        {"name": "BathroomsHalf", "type": "NUMERIC"},
        {"name": "BathroomsTotalInteger", "type": "NUMERIC"},
        {"name": "BedroomsTotal", "type": "NUMERIC"},
        {"name": "BuyerAgencyCompensation", "type": "STRING"},
        {"name": "BuyerAgencyCompensationType", "type": "STRING"},
        {"name": "BuyerOfficeKey", "type": "STRING"},
        {"name": "CoBuyerOfficeKey", "type": "STRING"},
        {"name": "CommunityFeatures", "type": "STRING", "mode": "REPEATED"},
        {"name": "ConstructionMaterials", "type": "STRING", "mode": "REPEATED"},
        {"name": "Cooling", "type": "STRING", "mode": "REPEATED"},
        {"name": "CountyOrParish", "type": "STRING"},
        {"name": "CoveredSpaces", "type": "NUMERIC"},
        {"name": "DirectionFaces", "type": "STRING"},
        {"name": "Disclosures", "type": "STRING", "mode": "REPEATED"},
        {"name": "ACT_ElementaryOther", "type": "STRING"},
        {"name": "ElementarySchool", "type": "STRING"},
        {"name": "ACT_EstimatedTaxes", "type": "STRING"},
        {"name": "ACT_ETJExtraTerritorialJurdn", "type": "STRING"},
        {"name": "ExteriorFeatures", "type": "STRING", "mode": "REPEATED"},
        {"name": "ACT_FEMAFloodPlain", "type": "STRING"},
        {"name": "Fencing", "type": "STRING", "mode": "REPEATED"},
        {"name": "FireplacesTotal", "type": "NUMERIC"},
        {"name": "Flooring", "type": "STRING", "mode": "REPEATED"},
        {"name": "FoundationDetails", "type": "STRING", "mode": "REPEATED"},
        {"name": "GarageSpaces", "type": "NUMERIC"},
        {"name": "GreenEnergyEfficient", "type": "STRING", "mode": "REPEATED"},
        {"name": "GreenSustainability", "type": "STRING", "mode": "REPEATED"},
        {"name": "ACT_GuestAccommodatonDesc", "type": "STRING"},
        {"name": "Heating", "type": "STRING", "mode": "REPEATED"},
        {"name": "HighSchool", "type": "STRING", "mode": "REPEATED"},
        {"name": "HorseAmenities", "type": "STRING", "mode": "REPEATED"},
        {"name": "HorseYN", "type": "BOOLEAN"},
        {"name": "ACT_IDXOptInYN", "type": "STRING"},
        {"name": "InteriorFeatures", "type": "STRING", "mode": "REPEATED"},
        {"name": "InternetAddressDisplayYN", "type": "BOOLEAN"},
        {"name": "InternetAutomatedValuationDisplayYN", "type": "BOOLEAN"},
        {"name": "InternetConsumerCommentYN", "type": "BOOLEAN"},
        {"name": "InternetEntireListingDisplayYN", "type": "BOOLEAN"},
        {"name": "ACT_LastChangeTimestamp", "type": "TIMESTAMP"},
        {"name": "ACT_LastChangeType", "type": "STRING"},
        {"name": "ACT_LastHumanModificationTimestamp", "type": "TIMESTAMP"},
        {"name": "ACT_LaundryLocation", "type": "STRING"},
        {"name": "Levels", "type": "STRING", "mode": "REPEATED"},
        {"name": "ListAgentAOR", "type": "STRING"},
        {"name": "ListAgentDirectPhone", "type": "STRING"},
        {"name": "ListAgentEmail", "type": "STRING"},
        {"name": "ListAgentFullName", "type": "STRING"},
        {"name": "ListAgentKey", "type": "STRING"},
        {"name": "ListAgentMlsId", "type": "STRING"},
        {"name": "ListAOR", "type": "STRING"},
        {"name": "ListingContractDate", "type": "STRING"},
        {"name": "ListingId", "type": "STRING"},
        {"name": "ListingKey", "type": "STRING"},
        {"name": "ListOfficeKey", "type": "STRING"},
        {"name": "ListOfficeMlsId", "type": "STRING"},
        {"name": "ListOfficeName", "type": "STRING"},
        {"name": "ListOfficePhone", "type": "STRING"},
        {"name": "ListPrice", "type": "NUMERIC"},
        {"name": "LivingArea", "type": "NUMERIC"},
        {"name": "LivingAreaSource", "type": "STRING"},
        {"name": "LotFeatures", "type": "STRING", "mode": "REPEATED"},
        {"name": "LotSizeAcres", "type": "NUMERIC"},
        {"name": "LotSizeSquareFeet", "type": "NUMERIC"},
        {"name": "MainLevelBedrooms", "type": "NUMERIC"},
        {"name": "MajorChangeTimestamp", "type": "TIMESTAMP"},
        {"name": "MajorChangeType", "type": "STRING"},
        {"name": "MiddleOrJuniorSchool", "type": "STRING"},
        {"name": "MLSAreaMajor", "type": "STRING"},
        {"name": "MlsStatus", "type": "STRING"},
        {"name": "NewConstructionYN", "type": "BOOLEAN"},
        {"name": "ACT_NumDining", "type": "STRING"},
        {"name": "ACT_NumLiving", "type": "STRING"},
        {"name": "ACT_OpenHouseCount", "type": "STRING"},
        {"name": "ACT_OpenHousePublicCount", "type": "STRING"},
        {"name": "OriginalEntryTimestamp", "type": "TIMESTAMP"},
        {"name": "OriginalListPrice", "type": "NUMERIC"},
        {"name": "OriginatingSystemName", "type": "STRING"},
        {"name": "OtherStructures", "type": "STRING", "mode": "REPEATED"},
        {"name": "ParcelNumber", "type": "STRING"},
        {"name": "ParkingFeatures", "type": "STRING", "mode": "REPEATED"},
        {"name": "ParkingTotal", "type": "NUMERIC"},
        {"name": "PatioAndPorchFeatures", "type": "STRING", "mode": "REPEATED"},
        {"name": "PoolFeatures", "type": "STRING", "mode": "REPEATED"},
        {"name": "PoolPrivateYN", "type": "BOOLEAN"},
        {"name": "PreviousListPrice", "type": "NUMERIC"},
        {"name": "PropertyCondition", "type": "STRING", "mode": "REPEATED"},
        {"name": "PropertySubType", "type": "STRING"},
        {"name": "PropertyType", "type": "STRING"},
        {"name": "PublicRemarks", "type": "STRING"},
        {"name": "Roof", "type": "STRING", "mode": "REPEATED"},
        {"name": "Sewer", "type": "STRING", "mode": "REPEATED"},
        {"name": "SpaFeatures", "type": "STRING", "mode": "REPEATED"},
        {"name": "SpecialListingConditions", "type": "STRING", "mode": "REPEATED"},
        {"name": "StandardStatus", "type": "STRING"},
        {"name": "ACT_StatusContractualSearchDate", "type": "STRING"},
        {"name": "SubAgencyCompensation", "type": "STRING"},
        {"name": "SubAgencyCompensationType", "type": "STRING"},
        {"name": "SubdivisionName", "type": "STRING"},
        {"name": "SyndicateTo", "type": "STRING", "mode": "REPEATED"},
        {"name": "SyndicationRemarks", "type": "STRING"},
        {"name": "TaxAssessedValue", "type": "NUMERIC"},
        {"name": "ACT_TaxFilledSqftTotal", "type": "STRING"},
        {"name": "TaxLegalDescription", "type": "STRING"},
        {"name": "TaxMapNumber", "type": "STRING"},
        {"name": "TaxYear", "type": "NUMERIC"},
        {"name": "ACT_UnitStyle", "type": "STRING"},
        {"name": "Utilities", "type": "STRING", "mode": "REPEATED"},
        {"name": "View", "type": "STRING", "mode": "REPEATED"},
        {"name": "VirtualTourURLUnbranded", "type": "STRING"},
        {"name": "WaterfrontFeatures", "type": "STRING", "mode": "REPEATED"},
        {"name": "WaterfrontYN", "type": "BOOLEAN"},
        {"name": "WaterSource", "type": "STRING", "mode": "REPEATED"},
        {"name": "WindowFeatures", "type": "STRING", "mode": "REPEATED"},
        {"name": "YearBuilt", "type": "NUMERIC"},
        {"name": "YearBuiltSource", "type": "STRING"},
        {"name": "ModificationTimestamp", "type": "TIMESTAMP"},
        {"name": "PhotosCount", "type": "NUMERIC"},
        {"name": "PhotosChangeTimestamp", "type": "TIMESTAMP"},
        {"name": "City", "type": "STRING"},
        {"name": "Country", "type": "STRING"},
        {"name": "Directions", "type": "STRING"},
        {"name": "Latitude", "type": "NUMERIC"},
        {"name": "Longitude", "type": "NUMERIC"},
        {"name": "PostalCode", "type": "STRING"},
        {"name": "StateOrProvince", "type": "STRING"},
        {"name": "StreetName", "type": "STRING"},
        {"name": "StreetNumber", "type": "STRING"},
        {"name": "StreetNumberNumeric", "type": "NUMERIC"},
        {"name": "StreetSuffix", "type": "STRING"},
        {"name": "UnparsedAddress", "type": "STRING"},
        {"name": "MlgCanView", "type": "BOOLEAN"},
    ],
)
