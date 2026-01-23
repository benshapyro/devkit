/*
INTEGRATION MAP TEMPLATE
Cadre AI branded artifact - Uses official Cadre brand colors

To customize: Replace CLIENT_NAME, DATE, and TOOL_DATA with actual client data.
See data-to-artifact.md for population instructions.
*/

import React, { useState } from "react";

// ============================================
// CUSTOMIZE THIS DATA FOR EACH CLIENT
// ============================================
const CLIENT_NAME = "Acme Corp";
const DATE = "December 30, 2024";

const TOOL_DATA = [
  { id: "salesforce", name: "Salesforce", category: "crm", upstream: ["webforms", "linkedin"], downstream: ["slack", "quickbooks"], connectionMethod: "native" },
  { id: "slack", name: "Slack", category: "communication", upstream: ["salesforce", "jira", "github"], downstream: [], connectionMethod: "native" },
  { id: "quickbooks", name: "QuickBooks", category: "finance", upstream: ["salesforce", "stripe"], downstream: ["excel"], connectionMethod: "api" },
  { id: "jira", name: "Jira", category: "project", upstream: ["github"], downstream: ["slack"], connectionMethod: "native" },
  { id: "github", name: "GitHub", category: "other", upstream: [], downstream: ["jira", "slack"], connectionMethod: "api" },
  { id: "webforms", name: "Web Forms", category: "other", upstream: [], downstream: ["salesforce"], connectionMethod: "api" },
  { id: "linkedin", name: "LinkedIn", category: "crm", upstream: [], downstream: ["salesforce"], connectionMethod: "ipaas" },
  { id: "stripe", name: "Stripe", category: "finance", upstream: [], downstream: ["quickbooks"], connectionMethod: "native" },
  { id: "excel", name: "Excel", category: "analytics", upstream: ["quickbooks"], downstream: [], connectionMethod: "manual" },
];
// ============================================

// Official Cadre Brand Colors
const COLORS = {
  black: "#0C0407",
  red: "#DB4545",
  blue: "#08749B",
  blueDark: "#034377",
  body: "#6E7191",
  muted: "#A1A1A1",
  warmWhite: "#FAF9F6",
  cream: "#F2EFE4",
  white: "#FFFFFF",
  border: "rgba(0, 0, 0, 0.10)",
};

const CATEGORY_COLORS = {
  crm: { bg: "#fef3c7", border: "#f59e0b", text: "#92400e" },
  communication: { bg: "#dbeafe", border: "#3b82f6", text: "#1e40af" },
  finance: { bg: "#d1fae5", border: "#10b981", text: "#065f46" },
  automation: { bg: "#f3e8ff", border: "#a855f7", text: "#6b21a8" },
  storage: { bg: "#e0e7ff", border: "#6366f1", text: "#3730a3" },
  project: { bg: "#fce7f3", border: "#ec4899", text: "#9d174d" },
  analytics: { bg: "#ccfbf1", border: "#14b8a6", text: "#0f766e" },
  other: { bg: "#f1f5f9", border: "#94a3b8", text: "#475569" },
};

const CONNECTION_STYLES = {
  native: { color: "#22c55e", label: "Native", dash: "0" },
  api: { color: COLORS.blue, label: "API", dash: "0" },
  ipaas: { color: "#a855f7", label: "iPaaS", dash: "5,5" },
  manual: { color: "#f59e0b", label: "Manual", dash: "2,2" },
};

export default function IntegrationMap() {
  const [selectedTool, setSelectedTool] = useState(null);
  
  // Calculate positions in a circular layout
  const getToolPositions = () => {
    const tools = TOOL_DATA;
    const centerX = 400;
    const centerY = 300;
    const radius = 200;
    
    return tools.map((tool, index) => {
      const angle = (index / tools.length) * 2 * Math.PI - Math.PI / 2;
      return {
        ...tool,
        x: centerX + radius * Math.cos(angle),
        y: centerY + radius * Math.sin(angle),
      };
    });
  };
  
  const toolPositions = getToolPositions();
  
  // Get all connections
  const getConnections = () => {
    const connections = [];
    toolPositions.forEach(tool => {
      tool.downstream.forEach(targetId => {
        const target = toolPositions.find(t => t.id === targetId);
        if (target) {
          connections.push({
            from: tool,
            to: target,
            method: tool.connectionMethod,
          });
        }
      });
    });
    return connections;
  };
  
  const connections = getConnections();
  
  // Highlight logic
  const isHighlighted = (tool) => {
    if (!selectedTool) return true;
    if (tool.id === selectedTool) return true;
    const selected = toolPositions.find(t => t.id === selectedTool);
    if (!selected) return false;
    return selected.upstream.includes(tool.id) || selected.downstream.includes(tool.id);
  };
  
  const isConnectionHighlighted = (conn) => {
    if (!selectedTool) return true;
    return conn.from.id === selectedTool || conn.to.id === selectedTool;
  };
  
  // Stats
  const stats = {
    totalTools: TOOL_DATA.length,
    totalConnections: connections.length,
    categories: [...new Set(TOOL_DATA.map(t => t.category))].length,
    nativeConnections: connections.filter(c => c.method === "native").length,
  };
  
  return (
    <div style={{ fontFamily: "'Inter', -apple-system, sans-serif", background: COLORS.warmWhite, minHeight: "100vh", padding: "1.5rem" }}>
      {/* Header */}
      <div style={{ 
        background: COLORS.black,
        color: COLORS.white,
        padding: "1.5rem",
        borderRadius: "16px",
        marginBottom: "1.5rem",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center"
      }}>
        <div>
          <h1 style={{ fontSize: "1.5rem", fontWeight: 600, margin: 0 }}>{CLIENT_NAME}</h1>
          <div style={{ color: COLORS.red, fontSize: "1rem", fontWeight: 500 }}>Integration Map</div>
        </div>
        <div style={{ textAlign: "right" }}>
          <div style={{ fontWeight: 700, fontSize: "0.875rem", letterSpacing: "0.05em" }}>
            CADRE<span style={{ color: COLORS.red }}>AI</span>
          </div>
          <div style={{ fontSize: "0.75rem", opacity: 0.7, marginTop: "0.25rem" }}>{DATE}</div>
        </div>
      </div>
      
      {/* Stats */}
      <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "1rem", marginBottom: "1.5rem" }}>
        {[
          { value: stats.totalTools, label: "Tools", accent: false },
          { value: stats.totalConnections, label: "Connections", accent: true },
          { value: stats.categories, label: "Categories", accent: false },
          { value: stats.totalConnections > 0 ? `${Math.round(stats.nativeConnections / stats.totalConnections * 100)}%` : "0%", label: "Native", accent: false },
        ].map((stat, i) => (
          <div key={i} style={{ 
            background: COLORS.white, 
            borderRadius: "16px", 
            padding: "1rem", 
            textAlign: "center",
            border: `1px solid ${COLORS.border}`,
            boxShadow: "0 28px 32px rgba(0,0,0,0.03)"
          }}>
            <div style={{ fontSize: "1.75rem", fontWeight: 600, color: stat.accent ? COLORS.red : COLORS.black, letterSpacing: "-0.03em" }}>{stat.value}</div>
            <div style={{ fontSize: "0.75rem", color: COLORS.body }}>{stat.label}</div>
          </div>
        ))}
      </div>
      
      {/* Legend */}
      <div style={{ 
        background: COLORS.white, 
        borderRadius: "12px", 
        padding: "1rem", 
        marginBottom: "1.5rem",
        display: "flex",
        flexWrap: "wrap",
        gap: "1rem",
        alignItems: "center",
        border: `1px solid ${COLORS.border}`,
        boxShadow: "0 28px 32px rgba(0,0,0,0.03)"
      }}>
        <strong style={{ fontSize: "0.75rem", color: COLORS.body }}>CATEGORIES:</strong>
        {Object.entries(CATEGORY_COLORS).map(([cat, colors]) => (
          <div key={cat} style={{ display: "flex", alignItems: "center", gap: "0.375rem" }}>
            <div style={{ 
              width: "12px", 
              height: "12px", 
              borderRadius: "4px", 
              background: colors.bg,
              border: `2px solid ${colors.border}`
            }} />
            <span style={{ fontSize: "0.7rem", color: COLORS.body, textTransform: "capitalize" }}>{cat}</span>
          </div>
        ))}
        <div style={{ borderLeft: `1px solid ${COLORS.border}`, height: "20px", margin: "0 0.5rem" }} />
        <strong style={{ fontSize: "0.75rem", color: COLORS.body }}>CONNECTIONS:</strong>
        {Object.entries(CONNECTION_STYLES).map(([method, style]) => (
          <div key={method} style={{ display: "flex", alignItems: "center", gap: "0.375rem" }}>
            <svg width="20" height="4">
              <line x1="0" y1="2" x2="20" y2="2" stroke={style.color} strokeWidth="2" strokeDasharray={style.dash} />
            </svg>
            <span style={{ fontSize: "0.7rem", color: COLORS.body }}>{style.label}</span>
          </div>
        ))}
      </div>
      
      {/* Map */}
      <div style={{ 
        background: COLORS.white, 
        borderRadius: "16px", 
        padding: "1rem",
        border: `1px solid ${COLORS.border}`,
        boxShadow: "0 28px 32px rgba(0,0,0,0.03)"
      }}>
        <svg width="100%" viewBox="0 0 800 600" style={{ display: "block" }}>
          {/* Arrow marker */}
          <defs>
            <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
              <polygon points="0 0, 10 3.5, 0 7" fill={COLORS.body} />
            </marker>
          </defs>
          
          {/* Connections */}
          {connections.map((conn, i) => {
            const style = CONNECTION_STYLES[conn.method] || CONNECTION_STYLES.api;
            const opacity = isConnectionHighlighted(conn) ? 1 : 0.15;
            
            const midX = (conn.from.x + conn.to.x) / 2;
            const midY = (conn.from.y + conn.to.y) / 2;
            const dx = conn.to.x - conn.from.x;
            const dy = conn.to.y - conn.from.y;
            const dist = Math.sqrt(dx*dx + dy*dy);
            const offset = dist * 0.15;
            const perpX = dist > 0 ? -dy / dist * offset : 0;
            const perpY = dist > 0 ? dx / dist * offset : 0;
            
            return (
              <path
                key={i}
                d={`M ${conn.from.x} ${conn.from.y} Q ${midX + perpX} ${midY + perpY} ${conn.to.x} ${conn.to.y}`}
                fill="none"
                stroke={style.color}
                strokeWidth="2"
                strokeDasharray={style.dash}
                opacity={opacity}
                markerEnd="url(#arrowhead)"
              />
            );
          })}
          
          {/* Tool Nodes */}
          {toolPositions.map((tool) => {
            const colors = CATEGORY_COLORS[tool.category] || CATEGORY_COLORS.other;
            const opacity = isHighlighted(tool) ? 1 : 0.3;
            const isSelected = tool.id === selectedTool;
            
            return (
              <g
                key={tool.id}
                transform={`translate(${tool.x}, ${tool.y})`}
                style={{ cursor: "pointer", opacity }}
                onClick={() => setSelectedTool(isSelected ? null : tool.id)}
              >
                <rect
                  x="-50"
                  y="-20"
                  width="100"
                  height="40"
                  rx="8"
                  fill={colors.bg}
                  stroke={isSelected ? COLORS.red : colors.border}
                  strokeWidth={isSelected ? 3 : 2}
                />
                <text
                  x="0"
                  y="5"
                  textAnchor="middle"
                  fill={colors.text}
                  fontSize="11"
                  fontWeight="600"
                  fontFamily="Inter, sans-serif"
                >
                  {tool.name.length > 12 ? tool.name.slice(0, 11) + "…" : tool.name}
                </text>
              </g>
            );
          })}
        </svg>
        
        {/* Selected Tool Details */}
        {selectedTool && (() => {
          const tool = toolPositions.find(t => t.id === selectedTool);
          if (!tool) return null;
          const upstreamTools = toolPositions.filter(t => tool.upstream.includes(t.id));
          const downstreamTools = toolPositions.filter(t => tool.downstream.includes(t.id));
          
          return (
            <div style={{ 
              marginTop: "1rem", 
              padding: "1rem", 
              background: COLORS.warmWhite, 
              borderRadius: "12px",
              borderLeft: `4px solid ${COLORS.red}`
            }}>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: "1rem" }}>
                <div>
                  <div style={{ fontWeight: 600, color: COLORS.black, marginBottom: "0.5rem" }}>{tool.name}</div>
                  <div style={{ fontSize: "0.875rem", color: COLORS.body }}>
                    Category: <span style={{ textTransform: "capitalize" }}>{tool.category}</span>
                  </div>
                  <div style={{ fontSize: "0.875rem", color: COLORS.body }}>
                    Connection: {CONNECTION_STYLES[tool.connectionMethod]?.label || tool.connectionMethod}
                  </div>
                </div>
                <div>
                  <div style={{ fontSize: "0.75rem", fontWeight: 600, color: COLORS.body, marginBottom: "0.5rem" }}>
                    RECEIVES DATA FROM ({upstreamTools.length})
                  </div>
                  {upstreamTools.length > 0 ? (
                    <div style={{ display: "flex", flexWrap: "wrap", gap: "0.25rem" }}>
                      {upstreamTools.map(t => (
                        <span key={t.id} style={{ 
                          padding: "0.25rem 0.5rem",
                          background: "#e0f2fe",
                          borderRadius: "6px",
                          fontSize: "0.75rem",
                        }}>{t.name}</span>
                      ))}
                    </div>
                  ) : (
                    <span style={{ fontSize: "0.75rem", color: COLORS.muted, fontStyle: "italic" }}>None (data source)</span>
                  )}
                </div>
                <div>
                  <div style={{ fontSize: "0.75rem", fontWeight: 600, color: COLORS.body, marginBottom: "0.5rem" }}>
                    SENDS DATA TO ({downstreamTools.length})
                  </div>
                  {downstreamTools.length > 0 ? (
                    <div style={{ display: "flex", flexWrap: "wrap", gap: "0.25rem" }}>
                      {downstreamTools.map(t => (
                        <span key={t.id} style={{ 
                          padding: "0.25rem 0.5rem",
                          background: "#d1fae5",
                          borderRadius: "6px",
                          fontSize: "0.75rem",
                        }}>{t.name}</span>
                      ))}
                    </div>
                  ) : (
                    <span style={{ fontSize: "0.75rem", color: COLORS.muted, fontStyle: "italic" }}>None (data sink)</span>
                  )}
                </div>
              </div>
            </div>
          );
        })()}
      </div>
      
      {/* Footer */}
      <div style={{ textAlign: "center", padding: "1rem", color: COLORS.muted, fontSize: "0.75rem" }}>
        Click any tool to see its connections · Prepared by <span style={{ color: COLORS.red }}>Cadre AI</span>
      </div>
    </div>
  );
}
