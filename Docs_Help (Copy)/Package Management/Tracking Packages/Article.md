# Tracking Packages

This guide covers how to track package status, handle delivery failures, capture proof of delivery, and understand exception statuses.

## Tracking Package Status

### Viewing Package Status Overview
1. **Package Grid View**:
   - Navigate to **Packages** in the main menu
   - Each package shows current status with color-coded indicators:
     - **Blue**: Pending pickup
     - **Yellow**: In transit
     - **Green**: Delivered successfully
     - **Red**: Exception/problem requiring attention

2. **Map View**:
   - Click the **Map** tab in the package view
   - Packages appear as markers on the map
   - Marker colors match status indicators
   - Click markers to see package details

### Detailed Package Tracking
1. **Open Package Details**:
   - Click on any package in the grid
   - This opens the package detail panel on the right

2. **View Tracking History**:
   - Click the **Events** tab in the detail panel
   - See complete chronological history of package movements
   - Each event shows date/time, location, and status change

### Real-Time Status Updates
- Status updates automatically as packages move through the system
- Refresh the page to see the latest information
- Notifications can be configured for status changes

## Understanding Package Statuses

### Primary Status Types

#### 1. Pending (Blue Marker)
- **Meaning**: Package created, waiting for pickup
- **Next Steps**: Package will be picked up during next scheduled route
- **Duration**: Typically same or next business day

#### 2. In Transit (Yellow Marker)
- **Meaning**: Package picked up and moving toward destination
- **Sub-statuses**:
  - Picked up from sender
  - At sorting facility
  - Out for delivery
- **Duration**: Varies by service level and distance

#### 3. Delivered (Green Marker)
- **Meaning**: Package successfully delivered to recipient
- **Proof Available**: Photos, signatures, or delivery confirmation
- **Final Status**: No further action needed

#### 4. Exception (Red Marker)
- **Meaning**: Problem preventing normal delivery
- **Requires Action**: Manual intervention needed
- **Common Reasons**: See "Exception Status Details" below

#### 5. On Hold (Orange Marker)
- **Meaning**: Delivery temporarily suspended
- **Reasons**: Customer request, payment issues, address problems
- **Resolution**: Address underlying issue to resume delivery

#### 6. Cancelled (Gray Marker)
- **Meaning**: Package cancelled before or during delivery
- **Reasons**: Customer request, undeliverable, returned to sender

### Tracking Event Details
Each tracking event includes:
- **Timestamp**: Exact date and time of event
- **Location**: Where the event occurred (city, facility, address)
- **Event Type**: Pickup, transit, delivery attempt, etc.
- **Description**: Detailed explanation of what happened
- **Reason Codes**: Specific codes for exceptions or delays

## Handling Package Delivery Failures

### When a Delivery Fails
1. **Automatic Notification**:
   - Status changes to "Exception" with red marker
   - Reason code explains the failure
   - Email notification sent (if configured)

### Common Delivery Failure Reasons
- **01 - No One Home**: Recipient not available
- **02 - Refused**: Recipient refused package
- **03 - Address Not Found**: Delivery address invalid
- **04 - Business Closed**: Commercial address closed
- **05 - Access Denied**: Cannot access delivery location
- **06 - Damaged Package**: Package damaged in transit
- **07 - Weather Delay**: Severe weather preventing delivery
- **08 - Vehicle Problem**: Delivery vehicle issue

### Resolving Delivery Failures

#### For "No One Home" (Reason 01)
1. **Automatic Retry**: System schedules redelivery attempt
2. **Contact Recipient**: Call or text for redelivery scheduling
3. **Hold at Facility**: Arrange pickup at local facility
4. **Safe Location**: Deliver to safe location if authorized

#### For "Address Not Found" (Reason 03)
1. **Verify Address**: Check address details with customer
2. **Update Address**: Modify delivery address if possible
3. **GPS Coordinates**: Provide specific coordinates if available
4. **Local Contact**: Arrange local contact for directions

#### For "Refused Delivery" (Reason 02)
1. **Contact Customer**: Understand reason for refusal
2. **Return to Sender**: Arrange return shipping
3. **Hold Package**: Keep at facility for customer pickup
4. **Alternative Recipient**: Deliver to alternate address if authorized

### Taking Action on Failed Deliveries
1. **Open Package Details**: Click on the exception package
2. **Review Failure Reason**: Check the latest tracking event
3. **Contact Customer**: Use contact information to reach recipient
4. **Update Delivery Instructions**: Modify special instructions if needed
5. **Schedule Redelivery**: Arrange new delivery attempt
6. **Add Tracking Event**: Document resolution actions taken

## Capturing Proof of Delivery

### Types of Proof Available
1. **Digital Photos**: Visual confirmation of package placement
2. **Electronic Signatures**: Customer signature on mobile device
3. **GPS Location**: Exact coordinates of delivery
4. **Timestamp**: Precise delivery date and time

### Taking Delivery Photos
1. **Access Photo Feature**:
   - Open package detail panel
   - Click **Photos** tab
   - Click **Add Photo** button

2. **Photo Requirements**:
   - Show package at delivery location
   - Include house number or business name if visible
   - Ensure photo is clear and well-lit
   - Take multiple angles if needed

3. **Upload Process**:
   - Select photo from device
   - Add description/notes
   - Click **Upload Photo**
   - Photo saves automatically to package record

### Collecting Electronic Signatures
1. **Signature Collection**:
   - Use mobile device or tablet
   - Customer signs directly on screen
   - Signature captures automatically
   - Links to package record immediately

2. **Signature Requirements**:
   - Clear, legible signature
   - Customer name printed below signature
   - Date and time automatically recorded
   - GPS location captured with signature

### Best Practices for Proof of Delivery
- **Always Take Photos**: Even for signature deliveries
- **Multiple Angles**: Show package, address, and context
- **Clear Documentation**: Add notes explaining unusual circumstances
- **Immediate Upload**: Don't wait to upload proof
- **Backup Methods**: Have multiple proof types when possible

## Understanding Exception Statuses

### What Causes Exception Status
- **Delivery Failures**: Cannot complete delivery as planned
- **Damaged Packages**: Package damage discovered
- **Address Issues**: Invalid or inaccessible delivery location
- **Customer Issues**: Recipient problems or requests
- **Weather/External**: Environmental factors preventing delivery
- **System Issues**: Technical problems affecting delivery

### Exception Resolution Process
1. **Immediate Assessment**:
   - Review exception reason code
   - Check package condition and location
   - Verify customer contact information

2. **Customer Communication**:
   - Contact recipient immediately
   - Explain the situation clearly
   - Discuss resolution options
   - Set expectations for next steps

3. **Resolution Actions**:
   - **Address Correction**: Update delivery address
   - **Redelivery Scheduling**: Arrange new delivery time
   - **Alternative Delivery**: Different location or method
   - **Return Processing**: Send back to sender if unresolvable

4. **Documentation**:
   - Add tracking event with resolution details
   - Update package status once resolved
   - Note any special instructions for future reference

### Preventing Future Exceptions
- **Address Validation**: Use address verification tools
- **Customer Communication**: Confirm delivery preferences
- **Clear Instructions**: Provide detailed delivery instructions
- **Backup Contacts**: Have alternative contact methods
- **Service Area Verification**: Ensure addresses are serviceable

## Advanced Tracking Features

### Bulk Status Updates
1. **Select Multiple Packages**: Use checkboxes in package grid
2. **Batch Actions**: Click batch actions menu
3. **Update Status**: Choose new status for all selected packages
4. **Add Notes**: Include explanation for status change

### Automated Notifications
- **Customer Notifications**: Automatic status updates via email/SMS
- **Internal Alerts**: Team notifications for exceptions
- **Escalation Rules**: Automatic escalation for unresolved issues
- **Custom Triggers**: Set up notifications for specific conditions

### Reporting and Analytics
- **Delivery Performance**: Success rates by area, driver, time
- **Exception Analysis**: Common failure reasons and trends
- **Customer Satisfaction**: Delivery time and quality metrics
- **Operational Metrics**: Efficiency and cost analysis

## Troubleshooting Tracking Issues

### Package Not Updating
- **Check Internet Connection**: Ensure system connectivity
- **Refresh Browser**: Clear cache and reload page
- **Contact Support**: If status seems incorrect
- **Verify Tracking Number**: Ensure correct package selected

### Missing Tracking Events
- **Driver Communication**: Check if events were properly recorded
- **System Sync**: Allow time for mobile device synchronization
- **Manual Entry**: Add missing events manually if needed
- **Technical Support**: Contact IT for system issues

## Next Steps
- Learn about [Package Modification](./Editing%20Packages.md)
- Set up [Delivery Notifications](./Messaging%20Tools%20and%20Overview.md)
- Configure [Dashboard Monitoring](./Dashboard%20KPIs%20and%20Metrics.md)