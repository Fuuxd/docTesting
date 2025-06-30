# Understanding Zones vs Operational Areas vs Delivery Areas

Learn the differences between the three types of geographic boundaries in Nearfleet Portal.

## Geographic Boundary Types

### Delivery Areas (Blue)
**Purpose:** Define where packages can be delivered
**Visibility:** Shown on dashboard map and Area Designer
**Function:** Determine package acceptance and routing
**Color:** Blue boundaries on map

### Operational Areas (Green)
**Purpose:** Define broader service regions for business operations  
**Visibility:** Management and reporting views
**Function:** Group delivery areas for analysis and planning
**Color:** Green boundaries when displayed

### Zones (Purple)
**Purpose:** High-level geographic divisions for administration
**Visibility:** Administrative panels and system configuration
**Function:** Organize operational areas and set regional policies
**Color:** Purple boundaries in admin views

## Hierarchy Structure

```
Zones (Largest)
├── Operational Areas
    ├── Delivery Areas (Smallest)
```

### Example Structure
- **Zone:** Greater Metropolitan Area
  - **Operational Area:** Downtown District
    - **Delivery Areas:** Financial District, Arts Quarter, Shopping Center
  - **Operational Area:** Suburban Region
    - **Delivery Areas:** North Suburbs, South Suburbs

## When to Use Each Type

### Delivery Areas
- **Package Creation:** System checks if delivery address falls within active delivery area
- **Route Planning:** Groups packages within same delivery area for efficiency
- **Service Levels:** Each delivery area can have different service options
- **Driver Assignment:** Assign specific drivers to delivery areas

### Operational Areas
- **Performance Reporting:** Analyze metrics across broader regions
- **Resource Allocation:** Plan driver and vehicle deployment
- **Cost Analysis:** Track expenses by operational region
- **Capacity Planning:** Understand volume across larger areas

### Zones
- **Administrative Control:** Set policies and permissions by major region
- **Regional Management:** Assign managers to oversee large geographic areas
- **System Configuration:** Configure settings that apply to entire zones
- **Strategic Planning:** High-level business analysis and planning

## Creating and Managing

### Delivery Areas (Most Common)
1. Use **Area Designer** drawing tools
2. Import from postal codes
3. Set service levels and priorities
4. Assign to drivers

### Operational Areas
1. Access via **Settings > Geographic Management**
2. Create from existing delivery areas
3. Define business regions
4. Set reporting parameters

### Zones (Administrative)
1. Available in **Admin Panel > Zone Management**
2. Create high-level geographic divisions
3. Assign operational areas to zones
4. Configure zone-specific policies

## Visual Identification

### On Dashboard Map
- **Blue Polygons:** Active delivery areas
- **Faded Blue:** Inactive delivery areas
- **Green Overlays:** Operational area boundaries (when enabled)
- **Purple Overlays:** Zone boundaries (admin view only)

### In Area Designer
- **Solid Lines:** Delivery area boundaries
- **Dashed Lines:** Operational area references
- **Dotted Lines:** Zone references

## Common Use Cases

### Small Business
- **Delivery Areas Only:** Simple setup with just delivery zones
- **Single Operational Area:** All delivery areas under one region
- **Single Zone:** Entire business coverage

### Multi-City Operations
- **Multiple Zones:** One per major city or region
- **Operational Areas:** Districts within each city
- **Delivery Areas:** Neighborhoods within districts

### Enterprise Operations
- **Geographic Zones:** States, provinces, or countries
- **Operational Areas:** Metro areas or major cities
- **Delivery Areas:** Specific neighborhoods or postal codes