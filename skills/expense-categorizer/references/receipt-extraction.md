# Receipt Data Extraction Guide

Best practices for extracting data from receipts using OCR and manual entry.

## Key Data Points

### Required Fields

| Field | Description | Example |
|-------|-------------|---------|
| **Merchant Name** | Business that issued receipt | "Starbucks #12345" |
| **Date** | Transaction date | "2026-01-05" |
| **Total Amount** | Final amount paid | "$45.67" |
| **Payment Method** | How it was paid | "Visa ending 1234" |

### Recommended Fields

| Field | Description | Example |
|-------|-------------|---------|
| **Line Items** | Individual purchases | "Latte - $5.50" |
| **Subtotal** | Amount before tax | "$40.00" |
| **Tax Amount** | Sales tax | "$3.20" |
| **Tip Amount** | Gratuity (if applicable) | "$8.00" |
| **Receipt Number** | Unique identifier | "TXN-123456789" |
| **Address** | Location of purchase | "123 Main St" |

### Contextual Fields (add manually)

| Field | Description | Example |
|-------|-------------|---------|
| **Business Purpose** | Why expense was incurred | "Client lunch - XYZ Corp" |
| **Attendees** | Who was present (meals) | "John Smith, Jane Doe" |
| **Project/Client** | Related project | "Project Alpha" |
| **Category** | Expense category | "Client Meals" |

---

## Receipt Types and Extraction Tips

### Restaurant Receipts

**Typical Layout:**
```
[Restaurant Name]
[Address]
[Phone]
------------------------
[Server Name]
Table: X
[Date] [Time]
------------------------
[Item 1]          $X.XX
[Item 2]          $X.XX
[Item 3]          $X.XX
------------------------
Subtotal          $XX.XX
Tax               $X.XX
------------------------
Total             $XX.XX
[Tip line - if credit card]
------------------------
[Payment info]
```

**Key Extraction Points:**
- Restaurant name (top)
- Date and time
- Subtotal (before tax)
- Tax amount
- Total (may or may not include tip)
- Tip amount (if on credit card slip)
- Payment method

**Common Issues:**
- Faded thermal paper
- Tip written by hand
- Two receipts (itemized + credit card slip)

**Best Practice:** Staple itemized receipt to credit card slip

### Hotel Receipts

**Typical Layout:**
```
[Hotel Name/Logo]
[Address]
------------------------
Guest: [Name]
Confirmation: [Number]
Check-in: [Date]
Check-out: [Date]
Room: [Number]
------------------------
Room Charges:
[Date] Room Rate      $XXX.XX
[Date] Room Rate      $XXX.XX
[Date] Tax            $XX.XX
------------------------
Incidentals:
[Date] Restaurant     $XX.XX
[Date] Parking        $XX.XX
------------------------
Total                 $XXX.XX
Payment: [Card type]
------------------------
```

**Key Extraction Points:**
- Hotel name
- Guest name (verify matches employee)
- Check-in and check-out dates
- Room rate per night
- Room tax
- Incidental charges (may need separate categorization)
- Total amount

**Common Issues:**
- Multi-page folios
- Incidentals mixed with room charges
- Currency conversion for international

**Best Practice:** Get itemized folio, not just credit card receipt

### Airline Receipts

**Typical Layout:**
```
[Airline Name]
------------------------
Passenger: [Name]
Confirmation: [Number]
------------------------
Flight: [Number]
[Origin] → [Destination]
[Date] [Time]
------------------------
Flight: [Number]
[Origin] → [Destination]
[Date] [Time]
------------------------
Fare:             $XXX.XX
Taxes/Fees:       $XX.XX
Baggage:          $XX.XX
------------------------
Total:            $XXX.XX
Payment: [Card]
```

**Key Extraction Points:**
- Airline name
- Passenger name
- Flight dates
- Origin and destination
- Fare breakdown
- Baggage fees
- Total amount

**Common Issues:**
- Confirmation email vs. actual receipt
- Multi-leg trips
- Changes and credits

**Best Practice:** Use e-receipt or confirmation page with payment info

### Uber/Lyft Receipts

**Typical Layout (email):**
```
[Service Logo]
------------------------
[Date] [Time]
[Pickup Address]
    ↓
[Dropoff Address]
------------------------
Trip fare:        $XX.XX
Tolls:            $X.XX
Service fee:      $X.XX
------------------------
Total:            $XX.XX
------------------------
Payment: [Card ending XXXX]
```

**Key Extraction Points:**
- Service name (Uber/Lyft)
- Date and time
- Pickup and dropoff locations
- Total fare
- Payment method

**Common Issues:**
- Email format varies
- Surge pricing not itemized
- Wait time charges

**Best Practice:** Forward email receipt to expense system

### Retail Receipts

**Typical Layout:**
```
[Store Name]
[Store Number/Address]
[Date] [Time]
------------------------
[Item 1] SKU     $X.XX
[Item 2] SKU     $X.XX
------------------------
Subtotal         $XX.XX
Tax              $X.XX
------------------------
Total            $XX.XX
[Payment method]
[Card ending XXXX]
```

**Key Extraction Points:**
- Store name
- Date
- Items (for categorization)
- Subtotal and tax
- Total
- Payment method

**Common Issues:**
- Long receipts with many items
- Abbreviations and SKUs
- Bundle/promo pricing

**Best Practice:** Highlight business items if mixed with personal

---

## OCR Best Practices

### Image Quality

| Factor | Recommendation |
|--------|---------------|
| **Resolution** | Minimum 300 DPI |
| **Lighting** | Even, no shadows |
| **Angle** | Flat, perpendicular to camera |
| **Focus** | Sharp, all text readable |
| **Cropping** | Receipt only, minimal background |

### Common OCR Errors

| Error Type | Example | Prevention |
|------------|---------|------------|
| **Number confusion** | 0/O, 1/l/I, 5/S | Verify against card statement |
| **Date format** | 01/05/26 vs 05/01/26 | Check context clues |
| **Currency symbols** | $ misread | Manual verification |
| **Decimal placement** | $1234 vs $12.34 | Reasonableness check |
| **Faded text** | ████ | Capture receipt promptly |

### Post-OCR Validation

1. **Verify merchant name** against known patterns
2. **Check date** is reasonable (not future, not ancient)
3. **Validate amounts** (subtotal + tax ≈ total)
4. **Confirm payment** matches employee's card
5. **Cross-reference** with bank statement

---

## Manual Entry Guidelines

### When to Enter Manually

- OCR fails or has low confidence
- Receipt is damaged or faded
- Non-standard format
- Foreign language receipts
- Handwritten receipts

### Data Entry Checklist

- [ ] Merchant name spelled correctly
- [ ] Date in correct format (YYYY-MM-DD)
- [ ] Amount includes correct decimal placement
- [ ] Currency is specified (if not USD)
- [ ] Payment method recorded
- [ ] Business purpose added
- [ ] Attendees listed (if meal/entertainment)
- [ ] Receipt image attached

### Handling Ambiguity

| Situation | Guidance |
|-----------|----------|
| Unreadable amount | Use bank statement, note discrepancy |
| Unclear merchant | Search for merchant online, use best match |
| Missing date | Use transaction date from card |
| Foreign currency | Record original + conversion rate |
| Multiple items | Itemize if different categories |

---

## Receipt Organization

### Digital Storage

**Naming Convention:**
```
YYYY-MM-DD_MerchantName_Amount.pdf
Example: 2026-01-05_Starbucks_45.67.pdf
```

**Folder Structure:**
```
/Expenses/
├── 2026/
│   ├── 01-January/
│   ├── 02-February/
│   └── ...
├── By Category/
│   ├── Travel/
│   ├── Meals/
│   └── ...
└── Pending/
```

### Physical Receipt Handling

1. **Capture immediately** - Thermal paper fades
2. **Photograph or scan** - Before fading
3. **Keep originals** - Until expense approved
4. **Store safely** - For audit period (3+ years)
5. **Match to reports** - Cross-reference to submissions

---

## Integration Patterns

### Email Receipts

Many vendors send e-receipts. Forward directly to expense system if supported.

**Common Sources:**
- Airlines (confirmation emails)
- Hotels (folio emails)
- Rideshare (trip receipts)
- Online purchases (order confirmations)
- Subscriptions (billing notices)

**Best Practice:** Set up email forwarding rules for known expense senders

### Credit Card Integration

Modern expense systems can auto-import transactions from corporate cards.

**Benefits:**
- Automatic transaction capture
- No duplicate entry
- Match to receipts
- Faster reconciliation

**Considerations:**
- Still need receipts for documentation
- Personal vs. business allocation
- Pending vs. posted transactions

### Mobile Capture

Most expense apps support mobile receipt capture.

**Tips:**
- Use good lighting
- Capture entire receipt
- Hold phone steady
- Review capture quality
- Add notes immediately while memory fresh

---

## Quality Assurance

### Pre-Submission Checklist

- [ ] All required fields populated
- [ ] Amounts are accurate
- [ ] Receipt image is clear and complete
- [ ] Business purpose is documented
- [ ] Category is appropriate
- [ ] Attendees listed (if applicable)
- [ ] No duplicate submissions
- [ ] Submitted within policy timeframe

### Common Rejection Reasons

| Reason | Prevention |
|--------|------------|
| Missing receipt | Attach at time of expense |
| Unreadable receipt | Recapture or get duplicate |
| Missing business purpose | Add before submitting |
| Incorrect category | Review category definitions |
| Amount mismatch | Verify against source |
| Missing attendees | List at time of meal |
| Personal expense | Separate before submitting |
| Duplicate submission | Check before adding |
