# Importing Multiple Packages from CSV Files

Upload and import multiple packages at once using CSV file format for efficient bulk package creation.

## Accessing Import Function

### From Main Menu
1. Click **Import** in the left navigation menu
2. You'll see the import files grid showing previous imports
3. Click **+ Upload New File** button in the toolbar

### From Package Management
1. Navigate to **Packages** menu
2. Click **Import** button in the package grid toolbar
3. Select **Package Import** from the dropdown options

## Preparing Your CSV File

### Required Columns
Your CSV file must include these columns with exact headers:
- **shiptoname**: Recipient's full name
- **shiptoaddress1**: Complete street address
- **shiptocity**: Destination city
- **shiptostate**: State or province abbreviation
- **shiptozip**: ZIP or postal code
- **shiptocontact**: Recipient phone number
- **shiptoemail**: Recipient email address
- **weight**: Package weight in pounds
- **servicelevel**: Delivery service type

### Optional Columns
Include these columns for additional package information:
- **shiptoaddress2**: Apartment, suite, or building number
- **length**: Package length in inches
- **width**: Package width in inches
- **height**: Package height in inches
- **declaredvalue**: Insurance value in dollars
- **deliveryinstructions**: Special delivery notes
- **clientreferenceid**: Your internal reference number
- **orderid**: Order management system reference

### Service Level Values
Use these exact values for the servicelevel column:
- **Standard**: 3-5 business day delivery
- **Express**: 1-2 business day delivery
- **Overnight**: Next business day delivery
- **Ground**: Economy ground shipping

## CSV File Format Requirements

### File Structure
- **Header Row**: First row must contain column names
- **Data Rows**: Each subsequent row represents one package
- **File Extension**: Must be .csv format
- **Character Encoding**: UTF-8 recommended

### Data Format Rules
- **No Empty Rows**: Remove any blank rows from the file
- **Consistent Quotes**: Use double quotes for text containing commas
- **Date Format**: Use MM/DD/YYYY for any date fields
- **Number Format**: Use decimal points for weights (e.g., 1.5)
- **No Special Characters**: Avoid non-standard characters

### Example CSV Structure
```
shiptoname,shiptoaddress1,shiptocity,shiptostate,shiptozip,shiptocontact,shiptoemail,weight,servicelevel
John Smith,123 Main Street,Anytown,CA,90210,555-123-4567,john@example.com,2.5,Standard
Jane Doe,456 Oak Avenue,Somewhere,NY,10001,555-987-6543,jane@example.com,1.0,Express
```

## Upload Process

### Step 1: File Selection
1. Click **Choose File** or **Browse** button
2. Navigate to your CSV file location
3. Select the CSV file
4. File name will appear in the upload field

### Step 2: Import Type Selection
1. **Import Type Dropdown**: Select "Package Import"
2. **File Validation**: System checks file format automatically
3. **Preview Option**: Some systems show first few rows for verification

### Step 3: File Upload
1. Click **Upload** button to send file to system
2. **Progress Bar**: Shows upload progress for large files
3. **Upload Confirmation**: System confirms successful file receipt

## Data Validation Process

### Automatic Validation
The system automatically checks:
- **Required Fields**: Ensures all mandatory columns have values
- **Address Validation**: Verifies delivery addresses are valid
- **Weight Limits**: Checks weights are within acceptable ranges
- **Service Level**: Confirms service types are supported
- **Data Format**: Validates phone numbers, emails, ZIP codes

### Validation Results Display
After upload, you'll see:
- **Total Rows**: Number of packages in the file
- **Valid Rows**: Number that passed validation
- **Error Rows**: Number with validation issues
- **Warning Rows**: Number with minor issues but processable

### Error Report
For rows with errors:
- **Row Number**: Which line in CSV has the problem
- **Error Type**: What kind of validation failed
- **Error Message**: Specific description of the issue
- **Suggested Fix**: Recommendation for correcting the error

## Processing Import

### Review and Confirm
1. **Validation Summary**: Review the validation results
2. **Error Resolution**: Fix any critical errors before processing
3. **Warning Review**: Decide whether to proceed with warnings
4. **Process Button**: Click "Process Import" to create packages

### Import Processing
- **Background Processing**: Import runs automatically
- **Progress Updates**: Status updates appear in import grid
- **Processing Time**: Depends on file size and system load
- **Completion Notification**: System alerts when finished

### Import Status Types
- **Uploaded**: File received, waiting for processing
- **Processing**: Currently creating packages from file
- **Completed**: All packages successfully created
- **Failed**: Import encountered errors and stopped
- **Partial**: Some packages created, others failed

## Post-Import Management

### Viewing Import Results
1. **Import Grid**: Shows all import files with status
2. **Click Import Name**: View detailed results
3. **Success Count**: Number of packages successfully created
4. **Error Count**: Number of rows that failed to process

### Package Verification
After successful import:
- **Package Grid**: New packages appear in main package list
- **Status**: All imported packages start with "Pending" status
- **Tracking Numbers**: System generates unique tracking numbers
- **Map Display**: Package locations show on dashboard map

### Error Resolution
For failed packages:
- **Error Report**: Download detailed error log
- **Fix Data**: Correct issues in original CSV
- **Re-import**: Upload corrected file
- **Manual Creation**: Create failed packages individually

## Import Best Practices

### File Preparation
- **Start Small**: Test with 10-20 packages first
- **Clean Data**: Remove duplicates and incomplete rows
- **Validate Addresses**: Verify addresses before import
- **Consistent Formatting**: Use same format throughout file

### Data Quality
- **Complete Information**: Fill all required fields
- **Accurate Weights**: Ensure weights are realistic
- **Valid Contacts**: Use working phone numbers and emails
- **Clear Instructions**: Write delivery instructions clearly

### Testing Strategy
- **Test File**: Create small test file before large import
- **Validation Check**: Review validation results carefully
- **Error Testing**: Include known errors to test validation
- **Performance Testing**: Test with larger files to check processing time

## Troubleshooting Common Issues

### File Upload Problems
- **File Size Limits**: Check maximum file size restrictions
- **Format Issues**: Ensure file is saved as CSV, not Excel
- **Character Encoding**: Save file with UTF-8 encoding
- **File Corruption**: Try re-saving and re-uploading file

### Validation Errors
- **Address Issues**: Use standard postal service formats
- **Missing Data**: Check for empty required fields
- **Invalid Characters**: Remove special symbols and characters
- **Format Consistency**: Ensure consistent data formatting

### Processing Failures
- **System Timeout**: Try smaller file sizes
- **Server Errors**: Wait and retry import
- **Data Conflicts**: Check for duplicate tracking numbers
- **Permission Issues**: Verify you have import permissions