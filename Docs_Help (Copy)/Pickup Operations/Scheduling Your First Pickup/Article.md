# Scheduling Your First Pickup

This guide walks you through creating and scheduling a pickup operation for package collection.

## Accessing Pickup Management

### From Main Menu
1. Click **Pickups** in the left navigation menu
2. You'll see the pickup management grid
3. Click **+ Add New Pickup** button in the toolbar

### From Dashboard
1. Click on the **Pickup Jobs** KPI card
2. This opens the pickup management interface
3. Click **+ Add New Pickup** to create

## Pickup Information Form

### Basic Pickup Details

**Pickup Name**
- Enter a descriptive name for this pickup route
- Example: "Downtown Morning Route" or "Warehouse Pickup #1"
- This helps identify the pickup in schedules and reports

**Pickup Date and Time**
- **Date**: Click calendar icon to select pickup date
- **Time Window**: Set start and end times for pickup availability
- **Example**: 9:00 AM - 11:00 AM pickup window

### Pickup Location Information

**Pickup Address**
- Enter the complete address where packages will be collected
- The system will validate and geocode the address automatically
- **Address Line 1**: Street address including building number
- **City, State, ZIP**: Will auto-populate from address validation

**Location Details**
- **Contact Name**: Person responsible at pickup location
- **Phone Number**: Contact number for pickup coordination
- **Access Instructions**: Special instructions for driver (gate codes, parking, etc.)

### Pickup Capacity and Constraints

**Vehicle Information**
- **Vehicle Type**: Select from available vehicle types (van, truck, etc.)
- **Weight Capacity**: Maximum weight the vehicle can handle
- **Volume Capacity**: Cubic feet or package count limits

**Driver Assignment**
- **Assign Driver**: Select from available drivers dropdown
- **Driver Qualifications**: System shows only qualified drivers
- **Automatic Assignment**: Leave blank for system to optimize assignment

## Package Selection for Pickup

### Available Packages Display
The system shows packages eligible for pickup:
- **Pending Packages**: Packages ready for collection
- **Location Match**: Packages at or near the pickup address
- **Service Level**: Packages requiring pickup by deadline

### Adding Packages to Pickup
1. **Select Packages**: Use checkboxes to select packages for this pickup
2. **Package Details**: Review package count, total weight, and volume
3. **Capacity Check**: System warns if selection exceeds vehicle capacity

### Package Information Shown
- **Tracking Number**: Unique package identifier
- **Delivery Address**: Where package will be delivered
- **Weight**: Individual package weight
- **Service Level**: Express, standard, overnight requirements
- **Special Handling**: Any special requirements or instructions

## Route Optimization

### Automatic Route Planning
- System calculates optimal pickup sequence
- **Distance Optimization**: Minimizes total travel distance
- **Time Optimization**: Considers traffic patterns and time windows
- **Capacity Optimization**: Ensures vehicle limits are respected

### Manual Route Adjustments
- **Drag and Drop**: Reorder pickup stops manually
- **Add Stops**: Include additional pickup locations
- **Remove Stops**: Exclude stops from current route
- **Time Adjustments**: Modify arrival time estimates

## Pickup Scheduling Options

### One-Time Pickup
- **Single Date**: Pickup occurs once on selected date
- **No Recurrence**: Must create new pickup for future dates

### Recurring Pickup
- **Daily**: Repeat every day at same time
- **Weekly**: Repeat on specific days of week
- **Monthly**: Repeat on specific dates each month
- **Custom Pattern**: Define custom recurrence schedule

### Recurring Pickup Settings
- **Start Date**: When recurring pattern begins
- **End Date**: When recurring pattern stops (optional)
- **Exceptions**: Skip specific dates (holidays, etc.)
- **Modifications**: Allow changes to individual instances

## Saving and Activating Pickup

### Validation Checks
Before saving, system validates:
- **Address Accuracy**: Pickup location is valid and accessible
- **Capacity Limits**: Total weight/volume within vehicle capacity
- **Time Feasibility**: Pickup window allows completion of route
- **Driver Availability**: Assigned driver is available during pickup time

### Save Process
1. Click **Save Pickup** button
2. System performs final validation
3. **Success Message**: "Pickup scheduled successfully"
4. Pickup appears in pickup grid and dashboard

### Pickup Status After Creation
- **Status**: Scheduled (purple marker on dashboard map)
- **Driver Notification**: Assigned driver receives pickup assignment
- **Package Updates**: Selected packages marked for pickup
- **Route Generation**: Optimized route created for driver

## Pickup Management After Creation

### Pickup Status Tracking
- **Scheduled**: Pickup created and waiting for execution
- **In Progress**: Driver has started pickup route
- **Completed**: All stops finished and packages collected
- **Exception**: Issues encountered requiring attention

### Modifying Scheduled Pickups
- **Add Packages**: Include additional packages in pickup
- **Change Time**: Modify pickup window if needed
- **Reassign Driver**: Change driver assignment
- **Cancel Pickup**: Remove pickup if no longer needed

### Real-Time Updates
- **Driver Location**: Track driver progress on map
- **Stop Completion**: Monitor pickup stop completion
- **Package Collection**: Confirm package pickup at each stop
- **Issue Reporting**: Handle exceptions and problems during pickup