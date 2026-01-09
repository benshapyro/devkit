/**
 * Cadre AI Component Kit (React + Tailwind)
 * 
 * Copy this file as starting point for Cadre-branded React artifacts.
 * All components use Cadre brand colors, typography, and spacing.
 * 
 * Usage: Import components or copy what you need into your artifact.
 */

import React, { useState } from 'react';

// ============================================
// BRAND TOKENS
// ============================================
// 
// Colors (use as Tailwind arbitrary values):
//   text-[#0C0407]     → Primary text, headlines
//   text-[#6E7191]     → Body text, descriptions
//   text-[#A1A1A1]     → Captions, metadata (decorative only)
//   bg-[#FAF9F6]       → Page background (warm white)
//   bg-[#F2EFE4]       → Section background (cream)
//   bg-[#FFFFFF]       → Cards, inputs
//   bg-[#0C0407]       → Primary buttons, dark sections, footer
//   bg-[#DB4545]       → Accent buttons, badges (max 10% of layout)
//   bg-[#08749B]       → Info accent, links
//   border-[#0C0407]/10 → Borders, dividers
//
// Typography:
//   font-['Inter',sans-serif] → All text
//   text-6xl tracking-[-0.03em] leading-[1.1] → Hero headlines (60px)
//   text-5xl tracking-[-0.03em] leading-[1.15] → Page titles (48px)
//   text-3xl tracking-[-0.02em] leading-[1.2] → Section headers (36px)
//   text-xl font-semibold leading-[1.5] → Subsection headers (20px)
//   text-lg leading-[1.6] → Lead paragraphs (18px)
//   text-base leading-[1.75] → Body text (16px)
//   text-sm leading-[1.5] → Small text, captions (14px)
//
// Spacing (8px base):
//   p-6 (24px) → Card padding
//   py-24 (96px) → Section vertical padding
//   gap-6 (24px) → Card grid gaps
//   gap-4 (16px) → Component gaps
//
// Radius:
//   rounded-full → Buttons (pill shape)
//   rounded-2xl → Cards (16px)
//   rounded-xl → Large cards (12px)
//   rounded-lg → Inputs (8px)
//   rounded-md → Tags, badges (6px)

// ============================================
// LAYOUT COMPONENTS
// ============================================

export const PageWrapper = ({ children, className = '' }) => (
  <div className={`min-h-screen bg-[#FAF9F6] font-['Inter',sans-serif] text-[#0C0407] ${className}`}>
    {children}
  </div>
);

export const Section = ({ children, className = '', cream = false }) => (
  <section className={`py-24 px-6 ${cream ? 'bg-[#F2EFE4]' : ''} ${className}`}>
    <div className="max-w-[1200px] mx-auto">
      {children}
    </div>
  </section>
);

export const SectionHeader = ({ label, title, description, className = '' }) => (
  <div className={`text-center max-w-[640px] mx-auto mb-16 ${className}`}>
    {label && (
      <p className="text-sm font-semibold text-[#6E7191] uppercase tracking-[0.05em] mb-4">
        {label}
      </p>
    )}
    <h2 className="text-5xl font-normal tracking-[-0.03em] leading-[1.15] text-[#0C0407] mb-4">
      {title}
    </h2>
    {description && (
      <p className="text-lg text-[#6E7191] leading-[1.6]">
        {description}
      </p>
    )}
  </div>
);

export const Container = ({ children, narrow = false, className = '' }) => (
  <div className={`mx-auto px-6 ${narrow ? 'max-w-[840px]' : 'max-w-[1200px]'} ${className}`}>
    {children}
  </div>
);

// ============================================
// BUTTON COMPONENTS
// ============================================

export const Button = ({ 
  children, 
  variant = 'primary', 
  size = 'default',
  className = '',
  ...props 
}) => {
  const variants = {
    primary: 'bg-[#0C0407] text-white hover:bg-[#1a1a1a]',
    accent: 'bg-[#DB4545] text-white hover:bg-[#c43d3d]',
    outline: 'bg-transparent text-[#0C0407] border border-[#0C0407]/15 hover:bg-[#0C0407]/5 hover:border-[#0C0407]/25',
    ghost: 'bg-transparent text-[#0C0407] hover:bg-[#0C0407]/5',
  };

  const sizes = {
    small: 'px-4 py-2 text-sm',
    default: 'px-6 py-3 text-base',
    large: 'px-8 py-4 text-lg',
  };

  return (
    <button
      className={`
        inline-flex items-center justify-center gap-2
        font-medium rounded-full
        transition-all duration-200 ease-out
        hover:-translate-y-0.5
        disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0
        ${variants[variant]}
        ${sizes[size]}
        ${className}
      `}
      {...props}
    >
      {children}
    </button>
  );
};

export const TextLink = ({ children, className = '', ...props }) => (
  <button
    className={`
      inline-flex items-center gap-1.5
      text-[#0C0407] font-medium
      hover:text-[#DB4545]
      transition-colors duration-150
      group
      ${className}
    `}
    {...props}
  >
    {children}
    <svg 
      className="w-4 h-4 transition-transform duration-200 group-hover:translate-x-1" 
      fill="none" 
      viewBox="0 0 24 24" 
      stroke="currentColor"
    >
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
    </svg>
  </button>
);

// ============================================
// CARD COMPONENTS
// ============================================

export const Card = ({ children, className = '', hover = true }) => (
  <div
    className={`
      bg-white p-6 rounded-2xl
      border border-[#0C0407]/10
      shadow-[0_1px_3px_rgba(0,0,0,0.08)]
      ${hover ? 'transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_8px_24px_rgba(0,0,0,0.12)]' : ''}
      ${className}
    `}
  >
    {children}
  </div>
);

export const FeatureCard = ({ icon, title, description, className = '' }) => (
  <Card className={`flex flex-col items-start ${className}`} hover={false}>
    {icon && (
      <div className="w-14 h-14 flex items-center justify-center bg-[#FAF9F6] rounded-2xl mb-6">
        {icon}
      </div>
    )}
    <h3 className="text-xl font-semibold text-[#0C0407] mb-3">{title}</h3>
    <p className="text-base text-[#6E7191] leading-[1.75]">{description}</p>
  </Card>
);

export const MetricCard = ({ value, label, change, className = '' }) => (
  <Card className={`text-center ${className}`} hover={false}>
    <div className="text-5xl font-semibold text-[#0C0407] tracking-[-0.03em] leading-[1.1] mb-2">
      {value}
    </div>
    <div className="text-base text-[#6E7191]">{label}</div>
    {change && (
      <div className={`text-sm font-medium mt-2 ${change.startsWith('+') ? 'text-green-600' : change.startsWith('-') ? 'text-red-600' : 'text-[#6E7191]'}`}>
        {change}
      </div>
    )}
  </Card>
);

export const ContentCard = ({ image, badge, title, description, meta, className = '' }) => (
  <Card className={`p-0 overflow-hidden ${className}`}>
    {image && (
      <div className="relative aspect-video">
        <img src={image} alt="" className="w-full h-full object-cover" />
        {badge && (
          <span className="absolute top-3 left-3 px-3 py-1.5 bg-[#DB4545] text-white text-xs font-medium rounded-md">
            {badge}
          </span>
        )}
      </div>
    )}
    <div className="p-6">
      <h3 className="text-xl font-semibold text-[#0C0407] mb-2">{title}</h3>
      {description && (
        <p className="text-sm text-[#6E7191] leading-[1.6] line-clamp-3 mb-3">
          {description}
        </p>
      )}
      {meta && (
        <p className="text-sm text-[#A1A1A1]">{meta}</p>
      )}
    </div>
  </Card>
);

// ============================================
// FORM COMPONENTS
// ============================================

export const Input = ({ label, error, className = '', ...props }) => (
  <div className={`flex flex-col gap-2 ${className}`}>
    {label && (
      <label className="text-sm font-medium text-[#0C0407]">{label}</label>
    )}
    <input
      className={`
        w-full px-4 py-3.5
        bg-white text-[#0C0407]
        border rounded-lg
        text-base
        placeholder:text-[#A1A1A1]
        transition-all duration-200
        focus:outline-none focus:ring-0
        ${error 
          ? 'border-[#DB4545] focus:border-[#DB4545] focus:shadow-[0_0_0_3px_rgba(219,69,69,0.1)]' 
          : 'border-[#0C0407]/15 focus:border-[#0C0407] focus:shadow-[0_0_0_3px_rgba(12,4,7,0.1)]'
        }
      `}
      {...props}
    />
    {error && (
      <p className="text-sm text-[#DB4545]">{error}</p>
    )}
  </div>
);

export const Select = ({ label, options, error, className = '', ...props }) => (
  <div className={`flex flex-col gap-2 ${className}`}>
    {label && (
      <label className="text-sm font-medium text-[#0C0407]">{label}</label>
    )}
    <select
      className={`
        w-full px-4 py-3.5
        bg-white text-[#0C0407]
        border rounded-lg
        text-base
        transition-all duration-200
        focus:outline-none focus:ring-0
        ${error 
          ? 'border-[#DB4545] focus:border-[#DB4545]' 
          : 'border-[#0C0407]/15 focus:border-[#0C0407]'
        }
      `}
      {...props}
    >
      {options.map((opt) => (
        <option key={opt.value} value={opt.value}>{opt.label}</option>
      ))}
    </select>
  </div>
);

// ============================================
// BADGE & TAG COMPONENTS
// ============================================

export const Badge = ({ children, variant = 'default', className = '' }) => {
  const variants = {
    default: 'bg-[#DB4545] text-white',
    subtle: 'bg-[#0C0407]/5 text-[#0C0407]',
    outline: 'bg-transparent border border-[#0C0407]/15 text-[#0C0407]',
  };

  return (
    <span className={`inline-flex px-3 py-1.5 text-xs font-medium rounded-md ${variants[variant]} ${className}`}>
      {children}
    </span>
  );
};

export const Tag = ({ children, active = false, onClick, className = '' }) => (
  <button
    onClick={onClick}
    className={`
      inline-flex items-center gap-1.5 px-3 py-1.5
      text-sm rounded-full
      transition-all duration-200
      ${active 
        ? 'bg-[#0C0407] text-white' 
        : 'bg-[#F8F8F8] text-[#6E7191] border border-[#0C0407]/10 hover:bg-[#F2EFE4]'
      }
      ${className}
    `}
  >
    {children}
  </button>
);

// ============================================
// NAVIGATION COMPONENTS
// ============================================

export const Header = ({ logo, navItems = [], cta, className = '' }) => (
  <header className={`sticky top-0 z-50 bg-white/95 backdrop-blur-sm border-b border-[#0C0407]/10 ${className}`}>
    <div className="max-w-[1200px] mx-auto px-6 py-4 flex items-center justify-between">
      <div className="flex items-center gap-8">
        {logo}
        <nav className="hidden md:flex items-center gap-8">
          {navItems.map((item, i) => (
            <a 
              key={i} 
              href={item.href}
              className="text-base font-medium text-[#0C0407] hover:text-[#DB4545] transition-colors"
            >
              {item.label}
            </a>
          ))}
        </nav>
      </div>
      {cta}
    </div>
  </header>
);

export const Footer = ({ logo, columns = [], bottom, className = '' }) => (
  <footer className={`bg-[#0C0407] text-white pt-16 pb-8 ${className}`}>
    <div className="max-w-[1200px] mx-auto px-6">
      <div className="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
        <div>{logo}</div>
        {columns.map((col, i) => (
          <div key={i}>
            <h4 className="text-sm font-semibold uppercase tracking-[0.05em] mb-4">{col.title}</h4>
            <ul className="space-y-3">
              {col.links.map((link, j) => (
                <li key={j}>
                  <a href={link.href} className="text-sm text-white/70 hover:text-white transition-colors">
                    {link.label}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
      {bottom && (
        <div className="pt-8 border-t border-white/10 text-sm text-white/50">
          {bottom}
        </div>
      )}
    </div>
  </footer>
);

// ============================================
// HERO COMPONENT
// ============================================

export const Hero = ({ 
  title, 
  titleAccent,
  description, 
  primaryCta, 
  secondaryCta,
  className = '' 
}) => (
  <section className={`py-24 px-6 bg-gradient-to-b from-[#F2EFE4] to-white text-center ${className}`}>
    <div className="max-w-[840px] mx-auto">
      <h1 className="text-6xl font-normal tracking-[-0.04em] leading-[1.1] text-[#0C0407] mb-6">
        {title}
        {titleAccent && <span className="text-[#DB4545]"> {titleAccent}</span>}
      </h1>
      {description && (
        <p className="text-lg text-[#6E7191] leading-[1.6] max-w-[560px] mx-auto mb-10">
          {description}
        </p>
      )}
      <div className="flex gap-4 justify-center">
        {primaryCta}
        {secondaryCta}
      </div>
    </div>
  </section>
);

// ============================================
// SLIDE COMPONENTS (for presentations)
// ============================================

export const SlideContainer = ({ children, currentSlide, totalSlides, onPrev, onNext, className = '' }) => (
  <div className={`min-h-screen bg-[#FAF9F6] font-['Inter',sans-serif] flex flex-col ${className}`}>
    <div className="flex-1 flex items-center justify-center p-8">
      {children}
    </div>
    <div className="flex items-center justify-between px-8 py-4 border-t border-[#0C0407]/10">
      <Button variant="ghost" onClick={onPrev} disabled={currentSlide === 0}>
        ← Previous
      </Button>
      <span className="text-sm text-[#6E7191]">
        {currentSlide + 1} / {totalSlides}
      </span>
      <Button variant="ghost" onClick={onNext} disabled={currentSlide === totalSlides - 1}>
        Next →
      </Button>
    </div>
  </div>
);

export const Slide = ({ children, className = '' }) => (
  <div className={`w-full max-w-[1000px] ${className}`}>
    {children}
  </div>
);

export const SlideTitle = ({ children, subtitle, className = '' }) => (
  <div className={`mb-12 ${className}`}>
    <h1 className="text-5xl font-normal tracking-[-0.03em] text-[#0C0407] mb-4">
      {children}
    </h1>
    {subtitle && (
      <p className="text-xl text-[#6E7191]">{subtitle}</p>
    )}
  </div>
);

// ============================================
// PRINT STYLES
// ============================================
// Add this CSS to your artifact for print support:
//
// @media print {
//   body { background: white !important; }
//   .no-print { display: none !important; }
//   .page-break { break-after: page; }
//   .avoid-break { break-inside: avoid; }
//   * { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
// }

// ============================================
// EXAMPLE USAGE
// ============================================

export default function CadreComponentDemo() {
  const [activeTag, setActiveTag] = useState('all');

  return (
    <PageWrapper>
      <Hero
        title="Component Kit"
        titleAccent="Demo"
        description="All Cadre brand components in one place. Copy what you need."
        primaryCta={<Button>Get started</Button>}
        secondaryCta={<TextLink>Learn more</TextLink>}
      />

      <Section>
        <SectionHeader
          label="Components"
          title="Everything you need"
          description="Built with Cadre brand tokens for consistent, professional output."
        />

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
          <MetricCard value="60%" label="Faster close" change="+12% vs last month" />
          <MetricCard value="$180K" label="Annual savings" />
          <MetricCard value="4/5" label="Milestones hit" />
        </div>

        <div className="flex gap-3 mb-8">
          {['all', 'buttons', 'cards', 'forms'].map(tag => (
            <Tag key={tag} active={activeTag === tag} onClick={() => setActiveTag(tag)}>
              {tag.charAt(0).toUpperCase() + tag.slice(1)}
            </Tag>
          ))}
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <Card>
            <h3 className="text-xl font-semibold mb-4">Buttons</h3>
            <div className="flex flex-wrap gap-3">
              <Button variant="primary">Primary</Button>
              <Button variant="accent">Accent</Button>
              <Button variant="outline">Outline</Button>
              <Button variant="ghost">Ghost</Button>
            </div>
          </Card>

          <Card>
            <h3 className="text-xl font-semibold mb-4">Form Elements</h3>
            <div className="space-y-4">
              <Input label="Email" placeholder="you@example.com" />
              <Select 
                label="Role" 
                options={[
                  { value: '', label: 'Select a role' },
                  { value: 'coo', label: 'COO' },
                  { value: 'cfo', label: 'CFO' },
                ]} 
              />
            </div>
          </Card>
        </div>
      </Section>
    </PageWrapper>
  );
}
