import { useState, useEffect, useCallback } from 'react';
import type { FilterState } from '../types';

const DEFAULT_FILTERS: FilterState = {
  search: '',
  groups: [],
  roles: [],
  tasks: [],
  favoritesOnly: false,
};

function parseArrayParam(params: URLSearchParams, key: string): string[] {
  return params.get(key)?.split(',').filter(Boolean) || [];
}

export function useUrlFilters() {
  const [filters, setFiltersState] = useState<FilterState>(() => {
    if (typeof window === 'undefined') {
      return DEFAULT_FILTERS;
    }

    const params = new URLSearchParams(window.location.search);
    return {
      search: params.get('q') || '',
      groups: parseArrayParam(params, 'groups'),
      roles: parseArrayParam(params, 'roles'),
      tasks: parseArrayParam(params, 'tasks'),
      favoritesOnly: params.get('favorites') === 'true',
    };
  });

  // Sync to URL
  useEffect(() => {
    const params = new URLSearchParams();
    if (filters.search) params.set('q', filters.search);
    if (filters.groups.length) params.set('groups', filters.groups.join(','));
    if (filters.roles.length) params.set('roles', filters.roles.join(','));
    if (filters.tasks.length) params.set('tasks', filters.tasks.join(','));
    if (filters.favoritesOnly) params.set('favorites', 'true');

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
        groups: parseArrayParam(params, 'groups'),
        roles: parseArrayParam(params, 'roles'),
        tasks: parseArrayParam(params, 'tasks'),
        favoritesOnly: params.get('favorites') === 'true',
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
