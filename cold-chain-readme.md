# Smart Cold Chain Monitor

## Overview
Smart Cold Chain Monitor is a real-time dashboard application for monitoring temperature-controlled supply chains. The system provides comprehensive monitoring, analytics, and AI-powered predictions for cold storage facilities, transport units, and distribution centers.

## Features

### Real-Time Monitoring
- Live temperature and humidity tracking across all locations
- Automated anomaly detection
- Risk score calculation for each facility
- Status indicators (Optimal, Warning, Critical)
- Interactive charts showing historical trends

### AI/ML Capabilities
- Predictive analytics for temperature and humidity trends
- Anomaly detection using statistical analysis
- Confidence scoring for predictions
- Trend analysis with seasonal adjustments
- Risk assessment modeling

### Dashboard Components
- Overview metrics (average temperature, humidity, active locations, alerts)
- Temperature and humidity trend charts
- Location-specific monitoring cards
- AI insights and predictions panel

### Automated Alerts
- Real-time anomaly notifications
- Critical threshold warnings
- Temperature and humidity deviation alerts
- Risk level indicators

## Technical Implementation

### Technologies Used
- HTML5
- CSS3 with custom variables
- Vanilla JavaScript
- Chart.js for data visualization
- Font Awesome for icons

### Key Classes

#### ColdChainMLModel
The core ML implementation class that handles:
- Time series predictions
- Anomaly detection
- Trend analysis
- Historical data management
- Confidence scoring

### Data Structure
```javascript
Location {
    id: string
    name: string
    type: string
    capacity: string
    sensors: string[]
    temp: number
    humidity: number
    analysis: AnomalyAnalysis
    prediction: Prediction
    trends: TrendAnalysis
    riskScore: number
}
```

## Setup and Installation

1. Ensure you have access to the following CDN resources:
   - Chart.js (v3.7.0)
   - Font Awesome (v6.0.0)

2. Include the required files:
   ```html
   <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
   <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.0/chart.min.js"></script>
   ```

3. Deploy the HTML file to your web server

## Usage

### Dashboard Navigation
- Main Dashboard: View overall metrics and charts
- Locations: Detailed view of individual facilities
- AI Insights: Access predictive analytics
- Settings: Configure system parameters

### Data Refresh
- Manual refresh available for individual components
- Automatic refresh every 30 seconds
- Loading indicators during data updates

### Monitoring Status Levels
- Optimal: Operating within ideal parameters
- Warning: Approaching threshold limits
- Critical: Exceeded acceptable ranges

## Risk Score Calculation

Risk scores are calculated based on multiple factors:
- Temperature range compliance
- Humidity level compliance
- Anomaly detection results
- Historical trend analysis

Formula:
```javascript
Base Score: 100
Deductions:
- Temperature < 2°C or > 8°C: -40 points
- Temperature < 3°C or > 7°C: -20 points
- Humidity < 30% or > 50%: -20 points
- Humidity < 35% or > 45%: -10 points
- Anomaly Detected: -15 points
```

## Customization

### Theme Variables
```css
--primary: #2563eb
--success: #22c55e
--warning: #f59e0b
--danger: #ef4444
--bg: #f8fafc
--card: #ffffff
--text: #1e293b
--text-light: #64748b
```

### Chart Configuration
Charts can be customized through the `commonOptions` object in the JavaScript code, including:
- Responsiveness
- Aspect ratio
- Legend display
- Grid styling
- Scale configuration

## Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with detailed description
4. Ensure code follows existing style conventions
5. Include tests for new functionality

## License

This project is licensed under the MIT License. See LICENSE file for details.
