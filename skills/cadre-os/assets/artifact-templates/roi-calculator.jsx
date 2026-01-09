/**
 * CADRE AI - ROI CALCULATOR
 * 
 * Interactive calculator for demonstrating AI implementation ROI.
 * Supports simple mode (3 inputs) and advanced mode (8 inputs).
 * 
 * Focus areas: Labor savings, error reduction, speed improvement, revenue impact
 */

import React, { useState, useMemo } from 'react';

export default function ROICalculator() {
  // Mode toggle
  const [advancedMode, setAdvancedMode] = useState(false);
  
  // Simple mode inputs
  const [hoursPerMonth, setHoursPerMonth] = useState(40);
  const [hourlyRate, setHourlyRate] = useState(75);
  const [expectedReduction, setExpectedReduction] = useState(60);
  
  // Advanced mode inputs
  const [errorRate, setErrorRate] = useState(5);
  const [errorCost, setErrorCost] = useState(500);
  const [implementationCost, setImplementationCost] = useState(150000);
  const [timelineMonths, setTimelineMonths] = useState(3);
  const [revenueImpact, setRevenueImpact] = useState(0);
  
  // Calculations
  const results = useMemo(() => {
    // Labor savings
    const monthlyLaborCost = hoursPerMonth * hourlyRate;
    const annualLaborCost = monthlyLaborCost * 12;
    const laborSavingsPercent = expectedReduction / 100;
    const annualLaborSavings = annualLaborCost * laborSavingsPercent;
    
    // Error savings (advanced)
    const monthlyErrors = hoursPerMonth * (errorRate / 100);
    const annualErrorCost = monthlyErrors * errorCost * 12;
    const annualErrorSavings = advancedMode ? annualErrorCost * laborSavingsPercent : 0;
    
    // Revenue impact (advanced)
    const annualRevenueImpact = advancedMode ? revenueImpact : 0;
    
    // Totals
    const totalAnnualSavings = annualLaborSavings + annualErrorSavings + annualRevenueImpact;
    const totalImplementationCost = advancedMode ? implementationCost : annualLaborSavings * 0.8; // Estimate if not provided
    
    // ROI metrics
    const paybackMonths = totalAnnualSavings > 0 
      ? (totalImplementationCost / (totalAnnualSavings / 12))
      : 0;
    
    const threeYearSavings = totalAnnualSavings * 3;
    const threeYearROI = totalImplementationCost > 0 
      ? ((threeYearSavings - totalImplementationCost) / totalImplementationCost) * 100
      : 0;
    
    const hoursReclaimed = hoursPerMonth * laborSavingsPercent * 12;
    
    return {
      annualLaborSavings,
      annualErrorSavings,
      annualRevenueImpact,
      totalAnnualSavings,
      totalImplementationCost,
      paybackMonths,
      threeYearSavings,
      threeYearROI,
      hoursReclaimed,
    };
  }, [hoursPerMonth, hourlyRate, expectedReduction, errorRate, errorCost, implementationCost, revenueImpact, advancedMode]);
  
  // Format helpers
  const formatCurrency = (val) => {
    if (val >= 1000000) return `$${(val / 1000000).toFixed(1)}M`;
    if (val >= 1000) return `$${Math.round(val / 1000)}K`;
    return `$${Math.round(val)}`;
  };
  
  const formatMonths = (val) => {
    if (val < 1) return `${Math.round(val * 30)} days`;
    if (val === 1) return '1 month';
    return `${val.toFixed(1)} months`;
  };

  return (
    <div 
      className="min-h-screen py-12 px-6"
      style={{ 
        backgroundColor: '#FAF9F6',
        fontFamily: "'Inter', -apple-system, sans-serif",
      }}
    >
      <div className="max-w-5xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <p 
            className="text-xs font-semibold uppercase tracking-widest mb-3"
            style={{ color: '#6E7191' }}
          >
            Cadre AI
          </p>
          <h1 
            className="text-5xl font-normal tracking-tight mb-4"
            style={{ color: '#0C0407', letterSpacing: '-0.03em' }}
          >
            AI ROI Calculator
          </h1>
          <p 
            className="text-lg max-w-xl mx-auto"
            style={{ color: '#6E7191' }}
          >
            Estimate the financial impact of automating a manual process with AI.
          </p>
        </div>
        
        {/* Mode Toggle */}
        <div className="flex justify-center mb-8">
          <div 
            className="inline-flex rounded-full p-1"
            style={{ backgroundColor: 'rgba(12, 4, 7, 0.05)' }}
          >
            <button
              onClick={() => setAdvancedMode(false)}
              className="px-5 py-2 rounded-full text-sm font-medium transition-all"
              style={{
                backgroundColor: !advancedMode ? '#0C0407' : 'transparent',
                color: !advancedMode ? '#FFFFFF' : '#6E7191',
              }}
            >
              Simple
            </button>
            <button
              onClick={() => setAdvancedMode(true)}
              className="px-5 py-2 rounded-full text-sm font-medium transition-all"
              style={{
                backgroundColor: advancedMode ? '#0C0407' : 'transparent',
                color: advancedMode ? '#FFFFFF' : '#6E7191',
              }}
            >
              Advanced
            </button>
          </div>
        </div>
        
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Inputs */}
          <div 
            className="rounded-2xl border p-8"
            style={{ 
              backgroundColor: '#FFFFFF',
              borderColor: 'rgba(12, 4, 7, 0.10)',
            }}
          >
            <h2 
              className="text-xl font-semibold mb-6"
              style={{ color: '#0C0407' }}
            >
              Your Inputs
            </h2>
            
            {/* Core Inputs (always shown) */}
            <div className="mb-2">
              <label className="block text-sm font-medium mb-2" style={{ color: '#0C0407' }}>
                Hours spent on this process per month
              </label>
              <div className="relative">
                <input
                  type="number"
                  value={hoursPerMonth}
                  onChange={(e) => setHoursPerMonth(parseFloat(e.target.value) || 0)}
                  className="w-full py-3.5 px-4 text-base rounded-lg border transition-all focus:outline-none"
                  style={{ borderColor: 'rgba(12, 4, 7, 0.15)', color: '#0C0407' }}
                />
                <span className="absolute right-4 top-1/2 -translate-y-1/2 text-base" style={{ color: '#A1A1A1' }}>
                  hrs
                </span>
              </div>
              <p className="text-xs mt-1.5" style={{ color: '#A1A1A1' }}>
                Include all team members involved
              </p>
            </div>
            
            <div className="mb-6 mt-6">
              <label className="block text-sm font-medium mb-2" style={{ color: '#0C0407' }}>
                Fully-loaded hourly cost
              </label>
              <div className="relative">
                <span className="absolute left-4 top-1/2 -translate-y-1/2 text-base" style={{ color: '#A1A1A1' }}>
                  $
                </span>
                <input
                  type="number"
                  value={hourlyRate}
                  onChange={(e) => setHourlyRate(parseFloat(e.target.value) || 0)}
                  className="w-full py-3.5 pl-8 pr-4 text-base rounded-lg border transition-all focus:outline-none"
                  style={{ borderColor: 'rgba(12, 4, 7, 0.15)', color: '#0C0407' }}
                />
              </div>
              <p className="text-xs mt-1.5" style={{ color: '#A1A1A1' }}>
                Salary + benefits + overhead (typically 1.3-1.5x salary)
              </p>
            </div>
            
            <div className="mb-6">
              <label className="block text-sm font-medium mb-2" style={{ color: '#0C0407' }}>
                Expected time reduction
              </label>
              <div className="relative">
                <input
                  type="number"
                  value={expectedReduction}
                  onChange={(e) => setExpectedReduction(Math.min(100, Math.max(0, parseFloat(e.target.value) || 0)))}
                  className="w-full py-3.5 px-4 text-base rounded-lg border transition-all focus:outline-none"
                  style={{ borderColor: 'rgba(12, 4, 7, 0.15)', color: '#0C0407' }}
                />
                <span className="absolute right-4 top-1/2 -translate-y-1/2 text-base" style={{ color: '#A1A1A1' }}>
                  %
                </span>
              </div>
              <p className="text-xs mt-1.5" style={{ color: '#A1A1A1' }}>
                Conservative estimate: 50-70% for most processes
              </p>
            </div>
            
            {/* Advanced Inputs */}
            {advancedMode && (
              <>
                <div 
                  className="border-t pt-6 mt-6"
                  style={{ borderColor: 'rgba(12, 4, 7, 0.10)' }}
                >
                  <h3 
                    className="text-sm font-semibold uppercase tracking-wide mb-4"
                    style={{ color: '#6E7191' }}
                  >
                    Error & Quality
                  </h3>
                  
                  <div className="mb-6">
                    <label className="block text-sm font-medium mb-2" style={{ color: '#0C0407' }}>
                      Current error rate
                    </label>
                    <div className="relative">
                      <input
                        type="number"
                        value={errorRate}
                        onChange={(e) => setErrorRate(parseFloat(e.target.value) || 0)}
                        className="w-full py-3.5 px-4 text-base rounded-lg border transition-all focus:outline-none"
                        style={{ borderColor: 'rgba(12, 4, 7, 0.15)', color: '#0C0407' }}
                      />
                      <span className="absolute right-4 top-1/2 -translate-y-1/2 text-base" style={{ color: '#A1A1A1' }}>
                        %
                      </span>
                    </div>
                  </div>
                  
                  <div className="mb-6">
                    <label className="block text-sm font-medium mb-2" style={{ color: '#0C0407' }}>
                      Average cost per error
                    </label>
                    <div className="relative">
                      <span className="absolute left-4 top-1/2 -translate-y-1/2 text-base" style={{ color: '#A1A1A1' }}>
                        $
                      </span>
                      <input
                        type="number"
                        value={errorCost}
                        onChange={(e) => setErrorCost(parseFloat(e.target.value) || 0)}
                        className="w-full py-3.5 pl-8 pr-4 text-base rounded-lg border transition-all focus:outline-none"
                        style={{ borderColor: 'rgba(12, 4, 7, 0.15)', color: '#0C0407' }}
                      />
                    </div>
                    <p className="text-xs mt-1.5" style={{ color: '#A1A1A1' }}>
                      Include rework time, customer impact, penalties
                    </p>
                  </div>
                </div>
                
                <div 
                  className="border-t pt-6 mt-6"
                  style={{ borderColor: 'rgba(12, 4, 7, 0.10)' }}
                >
                  <h3 
                    className="text-sm font-semibold uppercase tracking-wide mb-4"
                    style={{ color: '#6E7191' }}
                  >
                    Investment
                  </h3>
                  
                  <div className="mb-6">
                    <label className="block text-sm font-medium mb-2" style={{ color: '#0C0407' }}>
                      Implementation cost
                    </label>
                    <div className="relative">
                      <span className="absolute left-4 top-1/2 -translate-y-1/2 text-base" style={{ color: '#A1A1A1' }}>
                        $
                      </span>
                      <input
                        type="number"
                        value={implementationCost}
                        onChange={(e) => setImplementationCost(parseFloat(e.target.value) || 0)}
                        className="w-full py-3.5 pl-8 pr-4 text-base rounded-lg border transition-all focus:outline-none"
                        style={{ borderColor: 'rgba(12, 4, 7, 0.15)', color: '#0C0407' }}
                      />
                    </div>
                  </div>
                  
                  <div className="mb-6">
                    <label className="block text-sm font-medium mb-2" style={{ color: '#0C0407' }}>
                      Additional annual revenue impact
                    </label>
                    <div className="relative">
                      <span className="absolute left-4 top-1/2 -translate-y-1/2 text-base" style={{ color: '#A1A1A1' }}>
                        $
                      </span>
                      <input
                        type="number"
                        value={revenueImpact}
                        onChange={(e) => setRevenueImpact(parseFloat(e.target.value) || 0)}
                        className="w-full py-3.5 pl-8 pr-4 text-base rounded-lg border transition-all focus:outline-none"
                        style={{ borderColor: 'rgba(12, 4, 7, 0.15)', color: '#0C0407' }}
                      />
                    </div>
                    <p className="text-xs mt-1.5" style={{ color: '#A1A1A1' }}>
                      From faster processing, better customer experience, etc.
                    </p>
                  </div>
                </div>
              </>
            )}
          </div>
          
          {/* Results */}
          <div className="space-y-6">
            {/* Primary Results */}
            <div 
              className="rounded-2xl p-8"
              style={{ backgroundColor: '#0C0407' }}
            >
              <h2 
                className="text-sm font-semibold uppercase tracking-wide mb-6"
                style={{ color: 'rgba(255,255,255,0.5)' }}
              >
                Your Results
              </h2>
              
              <div className="text-center mb-8">
                <div 
                  className="text-6xl font-semibold tracking-tight mb-2"
                  style={{ color: '#FFFFFF', letterSpacing: '-0.03em' }}
                >
                  {formatCurrency(results.totalAnnualSavings)}
                </div>
                <div style={{ color: 'rgba(255,255,255,0.7)' }}>
                  Annual Savings
                </div>
              </div>
              
              <div className="grid grid-cols-2 gap-4">
                <div 
                  className="rounded-xl p-4 text-center"
                  style={{ backgroundColor: 'rgba(255,255,255,0.1)' }}
                >
                  <div 
                    className="text-2xl font-semibold mb-1"
                    style={{ color: '#FFFFFF' }}
                  >
                    {formatMonths(results.paybackMonths)}
                  </div>
                  <div 
                    className="text-sm"
                    style={{ color: 'rgba(255,255,255,0.6)' }}
                  >
                    Payback Period
                  </div>
                </div>
                <div 
                  className="rounded-xl p-4 text-center"
                  style={{ backgroundColor: 'rgba(255,255,255,0.1)' }}
                >
                  <div 
                    className="text-2xl font-semibold mb-1"
                    style={{ color: '#FFFFFF' }}
                  >
                    {Math.round(results.threeYearROI)}%
                  </div>
                  <div 
                    className="text-sm"
                    style={{ color: 'rgba(255,255,255,0.6)' }}
                  >
                    3-Year ROI
                  </div>
                </div>
              </div>
            </div>
            
            {/* Breakdown */}
            <div 
              className="rounded-2xl border p-8"
              style={{ 
                backgroundColor: '#FFFFFF',
                borderColor: 'rgba(12, 4, 7, 0.10)',
              }}
            >
              <h3 
                className="text-sm font-semibold uppercase tracking-wide mb-4"
                style={{ color: '#6E7191' }}
              >
                Savings Breakdown
              </h3>
              
              <div className="space-y-4">
                <div className="flex justify-between items-center py-3 border-b" style={{ borderColor: 'rgba(12,4,7,0.08)' }}>
                  <span style={{ color: '#6E7191' }}>Labor savings</span>
                  <span className="font-semibold" style={{ color: '#0C0407' }}>
                    {formatCurrency(results.annualLaborSavings)}/yr
                  </span>
                </div>
                
                {advancedMode && results.annualErrorSavings > 0 && (
                  <div className="flex justify-between items-center py-3 border-b" style={{ borderColor: 'rgba(12,4,7,0.08)' }}>
                    <span style={{ color: '#6E7191' }}>Error reduction</span>
                    <span className="font-semibold" style={{ color: '#0C0407' }}>
                      {formatCurrency(results.annualErrorSavings)}/yr
                    </span>
                  </div>
                )}
                
                {advancedMode && results.annualRevenueImpact > 0 && (
                  <div className="flex justify-between items-center py-3 border-b" style={{ borderColor: 'rgba(12,4,7,0.08)' }}>
                    <span style={{ color: '#6E7191' }}>Revenue impact</span>
                    <span className="font-semibold" style={{ color: '#0C0407' }}>
                      {formatCurrency(results.annualRevenueImpact)}/yr
                    </span>
                  </div>
                )}
                
                <div className="flex justify-between items-center py-3">
                  <span style={{ color: '#6E7191' }}>Hours reclaimed annually</span>
                  <span className="font-semibold" style={{ color: '#0C0407' }}>
                    {Math.round(results.hoursReclaimed)} hrs
                  </span>
                </div>
              </div>
            </div>
            
            {/* 3-Year View */}
            <div 
              className="rounded-2xl border p-8"
              style={{ 
                backgroundColor: '#FFFFFF',
                borderColor: 'rgba(12, 4, 7, 0.10)',
              }}
            >
              <h3 
                className="text-sm font-semibold uppercase tracking-wide mb-4"
                style={{ color: '#6E7191' }}
              >
                3-Year Projection
              </h3>
              
              <div className="grid grid-cols-3 gap-4 text-center">
                <div>
                  <div className="text-2xl font-semibold" style={{ color: '#0C0407' }}>
                    {formatCurrency(results.totalAnnualSavings)}
                  </div>
                  <div className="text-sm" style={{ color: '#A1A1A1' }}>Year 1</div>
                </div>
                <div>
                  <div className="text-2xl font-semibold" style={{ color: '#0C0407' }}>
                    {formatCurrency(results.totalAnnualSavings * 2)}
                  </div>
                  <div className="text-sm" style={{ color: '#A1A1A1' }}>Year 2</div>
                </div>
                <div>
                  <div className="text-2xl font-semibold" style={{ color: '#0C0407' }}>
                    {formatCurrency(results.threeYearSavings)}
                  </div>
                  <div className="text-sm" style={{ color: '#A1A1A1' }}>Year 3</div>
                </div>
              </div>
              
              <div 
                className="mt-6 pt-6 border-t text-center"
                style={{ borderColor: 'rgba(12,4,7,0.08)' }}
              >
                <div className="text-sm" style={{ color: '#6E7191' }}>
                  Net benefit after {formatCurrency(advancedMode ? implementationCost : results.totalImplementationCost)} investment
                </div>
                <div 
                  className="text-3xl font-semibold mt-2"
                  style={{ color: '#16a34a' }}
                >
                  {formatCurrency(results.threeYearSavings - (advancedMode ? implementationCost : results.totalImplementationCost))}
                </div>
              </div>
            </div>
          </div>
        </div>
        
        {/* CTA */}
        <div 
          className="mt-12 rounded-2xl p-8 text-center"
          style={{ backgroundColor: '#F2EFE4' }}
        >
          <h3 
            className="text-2xl font-normal mb-3"
            style={{ color: '#0C0407' }}
          >
            Ready to capture these savings?
          </h3>
          <p 
            className="mb-6"
            style={{ color: '#6E7191' }}
          >
            Let's talk about which processes have the highest ROI potential for your organization.
          </p>
          <button
            className="px-8 py-3 rounded-full font-medium transition-all hover:-translate-y-0.5"
            style={{ 
              backgroundColor: '#DB4545',
              color: '#FFFFFF',
            }}
          >
            Get started
          </button>
        </div>
        
        {/* Disclaimer */}
        <p 
          className="text-center mt-8 text-sm"
          style={{ color: '#A1A1A1' }}
        >
          These projections are estimates based on your inputs. Actual results may vary based on implementation complexity, adoption rates, and other factors.
        </p>
      </div>
      
      {/* Print Styles */}
      <style>{`
        @media print {
          body { background: white !important; }
          .no-print { display: none !important; }
          * { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
        }
      `}</style>
    </div>
  );
}
