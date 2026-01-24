import { Component, type ReactNode, type ErrorInfo } from 'react';

interface Props {
  children: ReactNode;
  fallback?: ReactNode;
}

interface State {
  hasError: boolean;
  error?: Error;
}

export class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('SkillGallery error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback || (
        <div className="p-6 border border-red-800 rounded-lg bg-red-900/20 text-center">
          <h2 className="text-lg font-semibold text-red-200">
            Something went wrong loading the gallery
          </h2>
          <p className="text-sm text-red-300 mt-2">
            Please refresh the page to try again.
          </p>
        </div>
      );
    }

    return this.props.children;
  }
}
