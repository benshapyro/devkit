import { useState, useEffect, useCallback } from 'react';
import type { FilterState } from '../types';

export function useUrlFilters() {
  const [filters, setFiltersState] = useState<FilterState>(() => {
    if (typeof window === 'undefined') {
      return { search: '', groups: [] };
    }

    const params = new URLSearchParams(window.location.search);
    return {
      search: params.get('q') || '',
      groups: params.get('groups')?.split(',').filter(Boolean) || [],
    };
  });

  // Sync to URL
  useEffect(() => {
    const params = new URLSearchParams();
    if (filters.search) params.set('q', filters.search);
    if (filters.groups.length) params.set('groups', filters.groups.join(','));

    const url = params.toString()
      ? `${window.location.pathname}?${params}`
      : window.location.pathname;

    window.history.replaceState({}, '', url);
  }, [filters]);

  // Handle back/forward
  useEffect(() => {
    const onPopState = () => {
      const params = new URLSearchParams(window.location.search);
      setFiltersState({
        search: params.get('q') || '',
        groups: params.get('groups')?.split(',').filter(Boolean) || [],
      });
    };
    window.addEventListener('popstate', onPopState);
    return () => window.removeEventListener('popstate', onPopState);
  }, []);

  const setFilters = useCallback((updates: Partial<FilterState>) => {
    setFiltersState(prev => ({ ...prev, ...updates }));
  }, []);

  return { filters, setFilters };
}
