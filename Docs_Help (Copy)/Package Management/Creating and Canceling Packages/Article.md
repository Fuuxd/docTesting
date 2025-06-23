# Creating and Canceling Packages

This guide will walk you through creating new packages, generating shipping labels, and importing multiple packages from CSV files.

## Creating a New Package for Delivery

### Step 1: Navigate to Package Management
1. From the main dashboard, click on **Packages** in the navigation menu
2. Click the **Add New Package** button (+ icon) in the package grid toolbar

### Step 2: Fill Out Package Information
The package creation form is divided into several sections:

#### Shipping Information
1. **Ship From Location**: Select or enter the pickup location
   - Use the dropdown to select from saved locations
   - Or enter a new address manually
   - The system will validate and geocode the address automatically

2. **Ship To Information**:
   - **Recipient Name**: Enter the full name of the recipient
   - **Address**: Enter the complete delivery address
   - **City, State, ZIP**: Will auto-populate based on address
   - **Phone Number**: Enter recipient's contact number
   - **Email**: Optional but recommended for delivery notifications

#### Package Details
1. **Package Dimensions**:
   - **Length**: Enter package length in inches
   - **Width**: Enter package width in inches  
   - **Height**: Enter package height in inches
   - **Weight**: Enter package weight in pounds

2. **Service Options**:
   - **Service Level**: Select delivery speed (Standard, Express, Overnight)
   - **Delivery Instructions**: Add any special delivery notes
   - **Signature Required**: Check if signature is needed

#### Additional Options
1. **Package Value**: Enter declared value for insurance
2. **Reference ID**: Add your internal tracking reference
3. **Order ID**: Link to your order management system

### Step 3: Validate and Save
1. Review all entered information
2. The system will validate addresses and show any warnings
3. Click **Save Package** to create the package
4. The system will generate a unique tracking number

### Package Status After Creation
- New packages start with **Pending** status (shown with blue marker)
- Package appears in your package grid immediately
- Tracking number is automatically generated

## Generating Shipping Labels

### For Individual Packages
1. **From Package Grid**:
   - Find your package in the grid
   - Click the **Actions** menu (three dots)
   - Select **Generate Label**

2. **From Package Detail View**:
   - Click on a package to open detail panel
   - Click the **Label** tab
   - Click **Generate New Label** button

### For Multiple Packages (Batch Labels)
1. **Select Multiple Packages**:
   - Use checkboxes to select packages in the grid
   - Or use **Select All** for all visible packages

2. **Create Label Batch**:
   - Click **Batch Actions** in the toolbar
   - Select **Create Label Batch**
   - Give your batch a descriptive name
   - Click **Generate Batch**

3. **Download Labels**:
   - Navigate to **Label Batches** in the main menu
   - Find your batch in the list
   - Click **Download PDF** to get all labels

### Label Information Included
- Recipient name and address
- Sender/return address
- Tracking number and barcode
- Service level and delivery instructions
- Package weight and dimensions
- QR code for mobile scanning

## Importing Multiple Packages from CSV

### Step 1: Prepare Your CSV File
Your CSV file must include these required columns:
- `shiptoname`: Recipient name
- `shiptoaddress1`: Street address
- `shiptocity`: City
- `shiptostate`: State/Province
- `shiptozip`: ZIP/Postal code
- `shiptocontact`: Phone number
- `shiptoemail`: Email address
- `weight`: Package weight
- `servicelevel`: Service type

### Optional CSV Columns
- `length`, `width`, `height`: Package dimensions
- `declaredvalue`: Insurance value
- `deliveryinstructions`: Special instructions
- `clientreferenceid`: Your reference number
- `orderid`: Order system reference

### Step 2: Upload the CSV File
1. Navigate to **Import** in the main menu
2. Click **Upload New File**
3. Select your CSV file
4. Choose **Package Import** as the import type
5. Click **Upload**

### Step 3: Validate Import Data
1. The system will preview your data
2. Review any validation errors or warnings
3. Correct any issues in your CSV file if needed
4. Click **Process Import** to create packages

### Step 4: Monitor Import Progress
1. The import runs in the background
2. You'll see progress updates in the Import Files grid
3. Once complete, all packages will appear in your package grid
4. Any errors will be reported in the import summary

### Import Best Practices
- **Test Small Batches First**: Start with 10-20 packages to test
- **Validate Addresses**: Ensure all addresses are complete and correct
- **Use Consistent Formatting**: Keep date and text formats consistent
- **Check Weight Units**: Ensure weights are in pounds
- **Avoid Special Characters**: Stick to standard ASCII characters

### Common Import Errors
- **Invalid Addresses**: Missing city, state, or ZIP code
- **Duplicate Tracking Numbers**: Each package needs unique tracking
- **Invalid Service Levels**: Use only supported service types
- **Missing Required Fields**: All required columns must have values
- **Format Issues**: Check date formats and number formats

## Managing Package Status

### Package Lifecycle
1. **Pending**: Package created, waiting for pickup
2. **In Transit**: Package picked up and moving
3. **Out for Delivery**: Package on delivery vehicle
4. **Delivered**: Package successfully delivered
5. **Exception**: Delivery issue requiring attention
6. **Cancelled**: Package cancelled before delivery

### Canceling a Package
1. **Before Pickup**:
   - Open package detail panel
   - Click **Actions** menu
   - Select **Cancel Package**
   - Confirm cancellation

2. **After Pickup**:
   - Contact customer service
   - May require return shipping
   - Cancellation fees may apply

### Modifying Package Information
1. **Before Pickup**: Most fields can be edited
2. **After Pickup**: Limited to delivery instructions and contact info
3. **In Transit**: Only contact information can be updated

## Troubleshooting Common Issues

### Address Validation Failures
- **Issue**: Address not recognized by system
- **Solution**: 
  - Verify address format and spelling
  - Try using standard USPS format
  - Contact support for manual validation

### Label Generation Errors
- **Issue**: Label won't generate
- **Solution**:
  - Check that all required package information is complete
  - Verify package dimensions and weight are valid
  - Ensure delivery address is validated

### CSV Import Failures
- **Issue**: Import file rejected
- **Solution**:
  - Check file format is CSV (not Excel)
  - Verify all required columns are present
  - Remove any empty rows or columns
  - Check for special characters in data

## Next Steps
- Learn about [Package Tracking](./Tracking%20Packages.md)
- Set up [Delivery Areas](./Creating%20and%20Importing%20Delivery%20Areas.md)
- Configure [Pickup Operations](./Setting%20Up%20Pickups.md)