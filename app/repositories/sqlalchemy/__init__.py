def _filter_deleted(query, model):
    """Helper to filter out soft-deleted records."""
    return query.where(model.deleted_at.is_(None))