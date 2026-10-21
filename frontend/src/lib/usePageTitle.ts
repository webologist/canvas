import { usePageMeta } from './usePageMeta'

/** Sets `document.title` to "<title> · V-Ideas" while the component is mounted. */
export function usePageTitle(title: string | null | undefined): void {
  usePageMeta({ title })
}
