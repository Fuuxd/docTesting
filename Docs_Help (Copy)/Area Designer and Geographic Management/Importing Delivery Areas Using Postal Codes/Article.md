# Importing Delivery Areas Using Postal Codes

Quickly create delivery areas by importing ZIP codes and postal boundaries.

## Accessing Import Tool

1. Open **Area Designer** from left menu
2. Click **Import** button in right panel
3. Select **Postal Codes** from dropdown
4. Import dialog opens

## Import Methods

### Single ZIP Code Entry
1. Type ZIP code in input field
2. Click **Add** to include in list
3. Repeat for additional ZIP codes
4. Click **Generate Areas** when complete

### Bulk ZIP Code Entry
1. Click **Bulk Entry** tab
2. Paste ZIP codes separated by commas
3. Example: `12345, 12346, 12347, 12348`
4. Click **Generate Areas**

### CSV File Upload
1. Click **Upload CSV** tab
2. Select CSV file with ZIP codes
3. Map columns if needed
4. Click **Import and Generate**

## CSV File Format

**Required Column:** ZIP_CODE or POSTAL_CODE
**Optional Columns:** AREA_NAME, SERVICE_LEVEL, PRIORITY

Example CSV:
```
ZIP_CODE,AREA_NAME,SERVICE_LEVEL
12345,Downtown,Express
12346,Suburbs,Standard
```

## Area Generation Process

### After Import
1. System processes postal boundaries
2. Creates individual areas for each ZIP code
3. Areas appear on map with default names
4. Generation progress bar shows status

### Default Settings
- **Area Names** - ZIP code number (e.g., "Area 12345")
- **Service Level** - Standard delivery
- **Status** - Active by default
- **Color** - Blue boundary

## Customizing Generated Areas

### Rename Areas
1. Double-click any generated area
2. Change name in properties dialog
3. Click **Update** to save

### Modify Service Levels
1. Select area from list
2. Change service level dropdown
3. Options: Standard, Express, Overnight

### Merge Adjacent Areas
1. Select multiple areas (hold Ctrl)
2. Right-click selection
3. Choose **Merge Areas**
4. Enter new combined area name

## Validation and Cleanup

### Overlap Detection
- System automatically checks for overlaps
- Red boundaries indicate conflicts
- Use **Resolve Overlaps** tool to fix

### Gap Analysis
- Yellow highlights show unserviced areas
- Add additional ZIP codes to fill gaps
- Use polygon tool for custom coverage

## Import Limitations

**ZIP Code Accuracy**
- Uses official postal service boundaries
- Some ZIP codes may not have defined boundaries
- Rural areas may have irregular shapes

**Processing Time**
- Large imports may take several minutes
- Progress bar shows completion status
- Areas appear on map as they're processed

## Common Issues

**ZIP Code Not Found**
- Verify ZIP code exists and is active
- Check for typos in code entry
- Some PO Box ZIP codes may not have boundaries

**Overlapping Areas**
- Multiple ZIP codes may share boundaries
- Use validation tools to identify conflicts
- Manual boundary adjustment may be needed